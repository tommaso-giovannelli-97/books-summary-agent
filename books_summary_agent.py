import openai
from serpapi import GoogleSearch
from newspaper import Article
from API_keys import OPEN_AI_KEY, SERPAPI_KEY

# Create the client once
client = openai.OpenAI(api_key=OPEN_AI_KEY)


def refine_query_with_gpt(user_query):
    prompt = f"""A user asked for books information with the query: "{user_query}".    
You have to understand if the user is trying to retrieve books information by book title, author or topic.    
Rewrite this into a more detailed and specific Google search query that will likely return high-quality book summaries from sites like Wikipedia, blogs, or review websites.
Do not include phrases like "user asked" or explanations — just the search query."""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that improves search engine queries for book summaries.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=50,
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()


def search_book_summary(query):
    print(f"🔍 Searching online for: {query}")

    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "num": 5,  # Max number of returned results
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    links = [res["link"] for res in results.get("organic_results", [])]

    return links[:3]  # top 3 results


def extract_article_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except:
        return None


def summarize_with_gpt(text, book_title):
    prompt = f"""Summarize the main ideas and contents of the book "{book_title}" based on the following extracted text from various online sources. The summary should be structured and meaningful, not just metadata or reviews.

Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that writes book content summaries.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=700,
        temperature=0.7,
    )

    return response.choices[0].message.content


def summarize_book(book_query):
    print(f"🎯 Original user query: {book_query}")
    refined_query = refine_query_with_gpt(book_query)
    refined_query = refined_query.replace('"', '') #To avoid unwanted quotes from ChatGPT output
    print(f"🔍 Refined search query: {refined_query}")

    urls = search_book_summary(refined_query)
    combined_text = ""

    print("\n🌐 Extracting content from sources...")
    for url in urls:
        content = extract_article_content(url)
        if content and len(content) > 300:
            combined_text += content[:3000]  # limit to avoid overload

    if not combined_text:
        print("❌ Could not extract sufficient content.")
        return

    print("\n✍️ Summarizing with GPT...")
    summary = summarize_with_gpt(combined_text, book_query)

    print("\n📘 Summary:")
    print(summary)


if __name__ == "__main__":
    query = input("Enter book title, author, or topic: ")
    summarize_book(query)
