# agent.py

from memory import load_memory, save_memory
from tools import get_news, write_file, read_file
from llm import call_ai
from db import add_memory, get_memory, clear_memory

# -------- DECISION ENGINE --------
def decide(user_input):
    text = user_input.lower()

    if text.startswith("news"):
        parts = user_input.split(" ", 1)

        if len(parts) > 1:
            return {"tool": "news", "query": parts[1]}
        else:
            return {"tool": "news", "query": ""}

    if text.startswith("write"):
        return {"tool": "write", "input": user_input}

    if "read" in text:
        return {"tool": "read"}

    return {"tool": "chat", "input": user_input}

# -------- EXECUTION ENGINE --------
def execute(plan):
    tool = plan["tool"]

    if tool == "news":
        return get_news()

    elif tool == "write":
        return write_file(plan["input"])

    elif tool == "read":
        return read_file()

    elif tool == "chat":
        return basic_chat(plan["input"])

    return "I don't understand."


# -------- BASIC CHAT (fallback AI) --------
def basic_chat(user_input):
    memory = load_memory()

    # build context
    history = ""
    for m in memory[-5:]:
        history += f"User: {m['user']}\nBot: {m['bot']}\n"

    prompt = f"""
Previous conversation:
{history}

User: {user_input}
Bot:
"""

    return call_ai(prompt)

# -------- MAIN AGENT --------
def agent(user_input, user_id="default"):

    # COMMANDS
    if user_input.startswith("/memory"):
        mem = get_memory(user_id)
        if not mem:
            return "No memory stored."

        return "\n".join([f"{i+1}. {m['content']}" for i, m in enumerate(mem)])

    if user_input.startswith("/clear"):
        clear_memory(user_id)
        return "Memory cleared."

    # NORMAL FLOW
    mem = get_memory(user_id)

    history = ""
    for m in mem[:5]:
        history += f"{m['content']}\n"

    prompt = f"""
Memory:
{history}

User: {user_input}
"""

    response = call_ai(prompt)

    # save memory
    add_memory(user_id, f"User: {user_input}")
    add_memory(user_id, f"Bot: {response}")

    return response
