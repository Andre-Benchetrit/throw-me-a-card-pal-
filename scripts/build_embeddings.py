import json
import sqlite3
from pathlib import Path
import numpy as np
from tqdm import tqdm
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.embedding_service import embed

CHUNKS_PATH = Path("data/chunks.json")
DB_PATH = Path("data/embeddings.db")


def build_database():
    print("Carregando chunks...")
    with open(CHUNKS_PATH, encoding="utf-8") as f:
        chunks = json.load(f)

    print("Criando banco SQLite...")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # recria a tabela do zero
    cur.execute("DROP TABLE IF EXISTS chunks")
    cur.execute("""
        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY,
            page INTEGER,
            text TEXT,
            embedding BLOB
        )
    """)

    conn.commit()

    print("Gerando embeddings com Gemini...")
    for chunk in tqdm(chunks, desc="Processando chunks"):
        text = chunk["text"]

        embedding = np.array(embed(text), dtype=np.float32)

        cur.execute(
            "INSERT INTO chunks (id, page, text, embedding) VALUES (?, ?, ?, ?)",
            (chunk["id"], chunk["page"], text, embedding.tobytes())
        )

    conn.commit()
    conn.close()
    print(f"\n✅ Banco recriado com sucesso em {DB_PATH}")


if __name__ == "__main__":
    build_database()
