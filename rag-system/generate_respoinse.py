# rag-system/generate_response.py
import os
import faiss
import numpy as np
import json
import openai
from openai.embeddings_utils import get_embedding

def load_vector_index(index_file="vector_index.index"):
    return faiss.read_index(index_file)

def load_chunks(chunks_file="chunks.json"):
    with open(chunks_file, "r", encoding="utf-8") as f:
        return json.load(f)

def retrieve_relevant_chunks(query, index, chunks, k=3):
    query_embedding = get_embedding(query, engine="text-embedding-ada-002")
    query_vector = np.array([query_embedding], dtype='float32')
    distances, indices = index.search(query_vector, k)
    results = [chunks[i] for i in indices[0] if i < len(chunks)]
    return results

def generate_response(query, context):
    system_prompt = "以下は参考となる文脈です:\n" + "\n".join(context)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content']

if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY")
    query = input("質問を入力してください: ")
    index = load_vector_index()
    chunks = load_chunks()
    context = retrieve_relevant_chunks(query, index, chunks)
    answer = generate_response(query, context)
    print("回答:", answer)
