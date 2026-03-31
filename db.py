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


def add_memory(user_id, pair, mem_type="short"):
    data = {
        "user_id": str(user_id),
        "type": mem_type,
        "pair": pair
    }
    requests.post(f"{URL}/rest/v1/memory", headers=HEADERS, json=data)


def get_memory(user_id, mem_type=None, limit=10):
    query = f"user_id=eq.{user_id}&order=id.desc&limit={limit}"

    if mem_type:
        query += f"&type=eq.{mem_type}"

    res = requests.get(
        f"{URL}/rest/v1/memory?{query}",
        headers=HEADERS
    )
    return res.json()


def delete_memory_by_id(mem_id):
    requests.delete(
        f"{URL}/rest/v1/memory?id=eq.{mem_id}",
        headers=HEADERS
    )


def clear_memory(user_id):
    requests.delete(
        f"{URL}/rest/v1/memory?user_id=eq.{user_id}",
        headers=HEADERS
    )
