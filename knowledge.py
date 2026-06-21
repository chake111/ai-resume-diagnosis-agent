from pathlib import Path

def load_knowledge():
    path = Path("knowledge/ai_agent_intern.txt")
    return path.read_text(encoding="utf-8")

def split_knowledge(text):
    return [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]