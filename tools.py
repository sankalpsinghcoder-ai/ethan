# tools.py

import requests
import os
from llm import call_ai


# -------- NEWS TOOL --------
API_KEY = os.getenv("GNEWS_API_KEY")

def get_news(query=""):
    try:
        url = f"https://gnews.io/api/v4/search?q={query}&lang=en&country=in&max=5&apikey={API_KEY}"

        res = requests.get(url).json()

        articles = res.get("articles", [])

        if not articles:
            return "No news found."

        results = []

        for art in articles:
            title = art["title"]
            desc = art["description"]
            link = art["url"]

            # 🔥 Better AI summary (using title + desc)
            summary = call_ai(f"""
Summarize this news in 2 lines:

Title: {title}
Description: {desc}
""")

            results.append(f"📰 {summary}\n🔗 {link}")

        return "\n\n".join(results)

    except Exception as e:
        return f"News error: {e}"


# -------- FILE WRITE --------
def write_file(text):
    with open("notes.txt", "a") as f:
        f.write(text + "\n")
    return "Saved to file."


# -------- FILE READ --------
def read_file():
    if not os.path.exists("notes.txt"):
        return "No file found."

    with open("notes.txt", "r") as f:
        return f.read()
