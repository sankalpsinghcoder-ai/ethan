from fastapi import FastAPI, Request
import requests
import os
from agent import agent

app = FastAPI()

TOKEN = os.getenv("TOKEN")  # we will set this in Railway

@app.get("/")
def home():
    return {"status": "running"}


@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()

    message = data.get("message", {}).get("text", "")
    chat_id = data["message"]["chat"]["id"]

    if message:
        reply = agent(message)
    else:
        reply = "Send text message."

    # send reply back to Telegram
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": reply
        }
    )

    return {"ok": True}
