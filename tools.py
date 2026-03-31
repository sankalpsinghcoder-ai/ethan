# tools.py

import requests
import os


# -------- NEWS TOOL --------
def get_news():
    api_key = os.getenv("NEWS_API_KEY")

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    
    try:
        data = requests.get(url).json()
        articles = data.get("articles", [])[:5]

        if not articles:
            return "No news found."

        news = "\n\n".join([f"• {a['title']}" for a in articles])
        return f"📰 Latest News:\n\n{news}"

    except Exception as e:
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
