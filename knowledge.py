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

def retrieve_knowledge(query, top_k = 2):
    chunks = split_knowledge(load_knowledge())
    keywords = query.lower().split()
    matched = [
        chunk for chunk in chunks
        if any(word in chunk.lower() for word in keywords)
    ]
    return matched[:top_k]