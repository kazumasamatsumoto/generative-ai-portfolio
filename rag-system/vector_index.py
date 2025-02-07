# rag-system/vector_index.py
import json
import numpy as np
import faiss
from openai.embeddings_utils import get_embedding  # 事前に必要なパッケージをインストール

def create_vector_index(chunks_file, index_file="vector_index.index"):
    with open(chunks_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    
    # 各チャンクの埋め込みを取得（text-embedding-ada-002 など）
    embeddings = [get_embedding(chunk, engine="text-embedding-ada-002") for chunk in chunks]
    embedding_dim = len(embeddings[0])
    
    # FAISS を使ってインデックスを構築
    index = faiss.IndexFlatL2(embedding_dim)
    index.add(np.array(embeddings, dtype='float32'))
    faiss.write_index(index, index_file)
    print("インデックス作成完了。", index_file)

if __name__ == "__main__":
    create_vector_index("chunks.json")
