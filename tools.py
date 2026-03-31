# tools.py

import requests
import os


# -------- NEWS TOOL --------
def get_news(query=""):
    base_url = "https://news.google.com/rss/search?q={}&hl=en-IN&gl=IN&ceid=IN:en"

    if query:
        url = base_url.format(query)
    else:
        url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"

    try:
        response = requests.get(url)
        text = response.text

        items = text.split("<item>")[1:6]

        results = []

        for item in items:
            title = item.split("<title>")[1].split("</title>")[0]
            link = item.split("<link>")[1].split("</link>")[0]

            results.append(f"📰 {title}\n🔗 {link}")

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
