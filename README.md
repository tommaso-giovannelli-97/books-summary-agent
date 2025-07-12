# 📘 AI Book Summary Agent

This is a Python demo project that uses the **OpenAI GPT API** and **SerpAPI** to search for and summarize books based on user queries (title, topic, or author). It retrieves real-world book summaries from online sources (like blogs, Wikipedia, review sites), processes them, and produces high-quality content summaries using GPT.

---

## 🚀 Features

- 🔍 Transforms user queries into effective Google search terms via GPT
- 🌐 Uses **SerpAPI** to search for book summaries
- 📰 Extracts readable text from web pages using `newspaper3k`
- ✍️ Generates clean, structured book summaries using GPT-4
- ✅ CLI-based interaction (easily extendable to a web UI)

---

## 🧰 Dependencies

Install all required packages with:

```bash
pip install -r requirements.txt
```

Or individually:

```bash
pip install openai serpapi newspaper3k lxml-html-clean
```

> Note: `lxml-html-clean` is required to fix a known compatibility issue in `newspaper3k`.

---

## 📦 `requirements.txt`

```
openai>=1.0.0
serpapi>=0.1.4
google-search-results>=2.4.2
newspaper3k==0.2.8
lxml-html-clean>=0.1.1
```

---

## 🔧 Setup

1. **Get API keys**:
   - OpenAI API Key: https://platform.openai.com/account/api-keys
   - SerpAPI Key: https://serpapi.com/

2. **Set up the project**:
   ```bash
   git clone https://github.com/your-username/books-summary-agent.git
   cd books-summary-agent
   pip install -r requirements.txt
   ```

3. **Edit API_keys file** and set your API keys:
   ```python
   OPEN_AI_KEY = "your_openai_key"
   SERPAPI_KEY = "your_serpapi_key"
   ```

---


Example interaction:

```
Enter book title, author, or topic: deep learning

🎯 Original user query: deep learning
🔍 Refined search query: best books on deep learning with summaries

🌐 Extracting content from sources...
✍️ Summarizing with GPT...

📘 Summary:
"Deep Learning" by Ian Goodfellow, Yoshua Bengio, and Aaron Courville provides a comprehensive overview...
```

---

## 🧠 How It Works

1. User enters a book-related query.
2. GPT-4 refines the query into a Google-friendly phrase.
3. SerpAPI fetches the top 3 organic search links.
4. `newspaper3k` extracts the readable text from these pages.
5. GPT-4 summarizes the combined content.

---

## 📜 License

MIT License