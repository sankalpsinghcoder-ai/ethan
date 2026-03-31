# tools.py

import requests
import os


# -------- NEWS TOOL --------
def get_news():
    return "News feature coming soon 📰"


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
