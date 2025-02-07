# RAG システム

このモジュールは、Retrieval-Augmented Generation (RAG) の実装例です。
ドキュメントの読み込み、チャンク化、ベクトルインデックスの構築、そして LLM を用いた応答生成の一連のフローを実現しています。

## 含まれる機能

- **ingest_documents.py**
  ドキュメントを読み込み、NLTK を利用して文単位に分割、指定チャンクサイズにまとめます
- **vector_index.py**
  各チャンクの埋め込みを取得し、FAISS を用いてベクトルインデックスを構築します
- **generate_response.py**
  ユーザーからのクエリに対して、インデックスから類似チャンクを取得し、LLM に渡して回答を生成します

## 環境構築

1. 仮想環境をアクティベートする
2. ルートディレクトリで依存ライブラリをインストール

   ```bash
   pip install -r ../requirements.txt
   ```

3. サンプルドキュメント（例: `sample.txt`）をプロジェクトルートに用意する

## 実行方法

1. ドキュメントのチャンク化:
   ```bash
   python ingest_documents.py
   ```
2. ベクトルインデックスの構築:
   ```bash
   python vector_index.py
   ```
3. クエリに対する応答生成:
   ```bash
   python generate_response.py
   ```

---

RAG システムの全体フローを確認しながら、実装をブラッシュアップしてください！
