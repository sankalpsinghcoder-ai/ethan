# tools.py

import requests
import os


# -------- NEWS TOOL --------
def get_news():
    url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"

    try:
        response = requests.get(url)
        text = response.text

        # simple parsing
        items = text.split("<item>")[1:6]

        news = []
        for item in items:
            title = item.split("<title>")[1].split("</title>")[0]
            news.append(f"• {title}")

        return "📰 Latest News:\n\n" + "\n\n".join(news)

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
