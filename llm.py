# llm.py

import requests
import os

API_KEY = os.getenv("GROQ_API_KEY")

def call_ai(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",  # best stable Groq model
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant. Answer clearly and directly without showing reasoning steps."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=120)
        result = response.json()

        # handle API errors
        if "choices" not in result:
            return f"AI error: {result}"

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"AI error: {str(e)}"
