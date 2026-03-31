# llm.py

import requests
import os

BASE = os.getenv("PROXY_URL")  # your worker URL


def call_ai(prompt):
    url = f"{BASE}/v1/chat/completions"

    payload = {
        "model": "gpt-oss-20b",   # 🔥 best model
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "metadata": {
            "reasoning_effort": "none"
        }
    }

    try:
        res = requests.post(url, json=payload, timeout=120)
        result = res.json()

        if "choices" not in result:
            return f"AI error: {result}"

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"AI error: {str(e)}"
