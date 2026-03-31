# agent.py

from memory import load_memory, save_memory
from tools import get_news, write_file, read_file


# -------- DECISION ENGINE --------
def decide(user_input):
    text = user_input.lower()

    if "news" in text:
        return {"tool": "news"}

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
    return f"You said: {user_input}"


# -------- MAIN AGENT --------
def agent(user_input):
    memory = load_memory()

    # Decide what to do
    plan = decide(user_input)

    # Execute action
    result = execute(plan)

    # Save memory
    memory.append({
        "user": user_input,
        "bot": result
    })
    save_memory(memory)

    return result
