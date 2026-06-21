from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_knowledge():
    path = Path("knowledge/ai_agent_intern.txt")
    return path.read_text(encoding="utf-8")


def split_knowledge(text):
    return [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]


def retrieve_knowledge(query, top_k=2):
    chunks = split_knowledge(load_knowledge())
    vectors = TfidfVectorizer(analyzer="char", ngram_range=(2, 4)).fit_transform(chunks + [query])
    scores = cosine_similarity(vectors[-1], vectors[:-1])[0]
    indexed = scores.argsort()[::-1][:top_k]
    return [chunks[i] for i in indexed if scores[i] > 0]