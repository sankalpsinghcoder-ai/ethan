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
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    # 🔥 Debug print (important)
    print("GROQ RESPONSE:", result)

    # Handle errors properly
    if "choices" not in result:
        return f"Error from AI: {result}"

    return result["choices"][0]["message"]["content"]
