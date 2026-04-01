# Ethan AI 🤖

Ethan AI is a cloud-based Telegram AI assistant built using Python, FastAPI, and modern LLM APIs.
It supports memory, tool usage, real-time news, and a modular agent architecture.

---

## 🚀 Features

* 💬 Chat-based AI assistant (Telegram bot)
* 🧠 Short-term & long-term memory (Supabase)
* 📰 Real-time news fetching with AI summaries
* 🧩 Tool-based architecture (agent + tools)
* 🔄 Context-aware conversations
* 🧹 Memory management:

  * `/memory`
  * `/memory short`
  * `/memory long`
  * `/clear`
  * `/clear <index>`
* ⚡ Fast cloud deployment (Railway)

---

## 🏗️ Architecture

Telegram → FastAPI (Webhook) → Agent → Tools / LLM → Database

### Components

| File       | Purpose                                 |
| ---------- | --------------------------------------- |
| `main.py`  | FastAPI webhook server                  |
| `agent.py` | Core agent logic (decision + execution) |
| `llm.py`   | LLM integration (Groq API)              |
| `tools.py` | Tools (news, file ops, etc.)            |
| `db.py`    | Supabase database operations            |
| `Procfile` | Railway deployment config               |

---

## 🧠 Agent Design

User Input
↓
Command Handling (/memory, /clear)
↓
Tool Routing (news, write, read)
↓
AI Response (fallback)
↓
Memory Storage

---

## 📦 Tech Stack

* Python (FastAPI)
* Telegram Bot API
* Groq LLM API
* Supabase (PostgreSQL)
* Railway (hosting)

---

## ⚙️ Setup

### 1. Clone repo

git clone https://github.com/sankalpsinghcoder-ai/ethan.git
cd ethan

---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Environment variables

Set these in your environment (or Railway):

TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_secret_key
GNEWS_API_KEY=your_news_api_key

---

### 4. Run locally

uvicorn main:app --host 0.0.0.0 --port 8000

---

### 5. Set Telegram Webhook

https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://your-app.up.railway.app/webhook

---

## 🧪 Usage

### Chat

hello
what is ai?

---

### News

news ai
news india

---

### Memory

/memory\n
/memory short\n
/memory long

---

### Clear memory

/clear\n
/clear 2

---

## 🧠 Memory System

* Short-term → recent conversation
* Long-term → important user facts
* Stored in Supabase
* Automatically used by AI

---

## 📰 News System

* Uses GNews API
* Fetches real-time news
* AI-generated summaries
* Includes source links

---

## ⚠️ Limitations

* Free API limits (Groq / GNews)
* Basic tool routing (not autonomous yet)
* No background scheduler yet

---

## 🔥 Future Improvements

* Autonomous agent loop (OpenClaw-style)
* Reminder scheduler system
* WhatsApp integration
* Vector memory (semantic search)
* Multi-model routing

---

## 👨‍💻 Author

Sankalp Singh
BCA Student | AI/ML & Infra Enthusiast
Jodhpur, Rajasthan

---

## ⭐ Support

If you like this project, consider starring the repo ⭐
