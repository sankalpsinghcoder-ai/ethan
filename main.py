# main.py

from fastapi import FastAPI, Request
import requests
import os
from agent import agent

app = FastAPI()

# Get token from Railway environment
TOKEN = os.getenv("TOKEN")


# -------- HEALTH CHECK --------
@app.get("/")
def home():
    return {"status": "running"}


# -------- TELEGRAM WEBHOOK --------
@app.post("/webhook")
async def telegram_webhook(req: Request):
    try:
        data = await req.json()

        # Extract message safely
        message = data.get("message", {}).get("text", "")
        chat_id = data.get("message", {}).get("chat", {}).get("id")

        # If no valid message
        if not chat_id:
            return {"ok": True}

        if message:
            reply = agent(message)
        else:
            reply = "Send text message."

        # Send reply to Telegram
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        requests.post(
            url,
            json={
                "chat_id": chat_id,
                "text": reply
            }
        )

        return {"ok": True}

    except Exception as e:
        print("ERROR:", e)
        return {"ok": False}
