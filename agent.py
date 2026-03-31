# agent.py

from tools import get_news, write_file, read_file
from llm import call_ai
from db import add_memory, get_memory, clear_memory, delete_memory_by_id


# -------- DECISION ENGINE --------
def decide(user_input):
    text = user_input.lower()

    if text.startswith("news"):
        parts = user_input.split(" ", 1)
        query = parts[1] if len(parts) > 1 else ""
        return {"tool": "news", "query": query}

    if text.startswith("write"):
        return {"tool": "write", "input": user_input}

    if "read" in text:
        return {"tool": "read"}

    return {"tool": "chat", "input": user_input}


# -------- EXECUTION ENGINE --------
def execute(plan):
    tool = plan["tool"]

    if tool == "news":
        return get_news(plan.get("query", ""))

    elif tool == "write":
        return write_file(plan["input"])

    elif tool == "read":
        return read_file()

    elif tool == "chat":
        return None  # handled later

    return "I don't understand."


# -------- MAIN AGENT --------
def agent(user_input, user_id="default"):

    # -------- MEMORY VIEW --------
    if user_input.startswith("/memory"):
        parts = user_input.split()

        mem_type = None
        if len(parts) > 1 and parts[1] in ["short", "long"]:
            mem_type = parts[1]

        mem = get_memory(user_id, mem_type)

        if not mem:
            return "No memory found."

        return "\n\n".join([
            f"{i+1}) [{m['type']}] {m['pair']}"
            for i, m in enumerate(mem)
        ])

    # -------- CLEAR MEMORY --------
    if user_input.startswith("/clear"):
        parts = user_input.split()

        # clear all
        if len(parts) == 1:
            clear_memory(user_id)
            return "All memory cleared."

        # clear by index
        try:
            index = int(parts[1]) - 1
            mem = get_memory(user_id)

            if index < 0 or index >= len(mem):
                return "Invalid index."

            delete_memory_by_id(mem[index]["id"])
            return f"Deleted memory {index+1}"

        except:
            return "Usage: /clear or /clear 2"

    # -------- TOOL ROUTING --------
    plan = decide(user_input)

    if plan["tool"] != "chat":
        result = execute(plan)

        pair = f"User: {user_input}\nBot: {result}"
        add_memory(user_id, pair, "short")

        return result

    # -------- FETCH MEMORY --------
    short_mem = get_memory(user_id, "short", 5)
    long_mem = get_memory(user_id, "long", 5)

    short_context = "\n".join([m["pair"] for m in short_mem])
    long_context = "\n".join([m["pair"] for m in long_mem])

    # -------- AI PROMPT --------
    prompt = f"""
You are Ethan, an intelligent Telegram AI assistant.

Use long-term memory ONLY if relevant.

Long-term memory:
{long_context}

Recent conversation:
{short_context}

User: {user_input}
"""

    response = call_ai(prompt)

    # -------- STORE SHORT MEMORY --------
    pair = f"User: {user_input}\nBot: {response}"
    add_memory(user_id, pair, "short")

    # -------- AUTO LONG MEMORY --------
    if any(word in user_input.lower() for word in [
        "my name", "i am", "i live", "remember", "my age", "i study"
    ]):
        add_memory(user_id, pair, "long")

    return response
