import json
import os

TODO_FILE = "logs/todo.json"

def load_todos():
    try:
        with open(TODO_FILE, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_todos(todos):
    os.makedirs("logs", exist_ok=True)
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2, ensure_ascii=False)
