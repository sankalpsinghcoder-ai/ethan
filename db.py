# db.py

import requests
import os

URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")

HEADERS = {
    "apikey": KEY,
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json"
}


def add_memory(user_id, content, mem_type="short"):
    data = {
        "user_id": str(user_id),
        "type": mem_type,
        "content": content
    }
    requests.post(f"{URL}/rest/v1/memory", headers=HEADERS, json=data)


def get_memory(user_id, limit=10):
    res = requests.get(
        f"{URL}/rest/v1/memory?user_id=eq.{user_id}&order=id.desc&limit={limit}",
        headers=HEADERS
    )
    return res.json()


def clear_memory(user_id):
    requests.delete(
        f"{URL}/rest/v1/memory?user_id=eq.{user_id}",
        headers=HEADERS
    )
