# rag-system/ingest_documents.py
import json
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def chunk_document(file_path, chunk_size=5):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    sentences = sent_tokenize(text)
    chunks = [' '.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]
    return chunks

if __name__ == "__main__":
    file_path = "sample.txt"  # リポジトリ内に用意するサンプルテキスト
    chunks = chunk_document(file_path)
    with open("chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=4)
    print("チャンク生成完了。chunks.json を確認してください。")
