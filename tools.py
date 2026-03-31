# tools.py

import requests
import os
from llm import call_ai


# -------- NEWS TOOL --------
def get_news(query=""):
    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

    try:
        res = requests.get(url)
        text = res.text

        items = text.split("<item>")[1:4]  # keep 3 (avoid overload)

        results = []

        for item in items:
            title = item.split("<title>")[1].split("</title>")[0]
            link = item.split("<link>")[1].split("</link>")[0]

            # 🔥 AI summary
            summary = call_ai(f"Summarize this news headline briefly:\n{title}")

            results.append(f"📰 {summary}\n🔗 {link}")

        return "\n\n".join(results)

    except:
        return "Error fetching news."


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
