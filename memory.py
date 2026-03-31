# memory.py

import json
import os

FILE = "memory.json"

def load_memory():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory(data):
    with open(FILE, "w") as f:
        json.dump(data[-20:], f, indent=2)  # keep last 20 messages
