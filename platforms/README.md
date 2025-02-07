# プラットフォーム連携モジュール

このモジュールは、生成 AI プロダクトにおける各種外部プラットフォームとの連携例を示します。
具体的な連携対象としては、以下のサンプルコードが含まれています。

## 含まれるサンプル

- **langchain_demo.py**
  LangChain を利用した基本的な LLM 連携例
- **amazon_bedrock_integration.py**
  Amazon Bedrock との連携サンプル（ひな形）
- **vertex_ai_integration.py**
  Vertex AI との連携サンプル（ひな形）

## 環境構築

1. 仮想環境をアクティベートする
2. ルートディレクトリで依存ライブラリをインストール
   ```bash
   pip install -r ../requirements.txt
   ```

````

3. プロジェクトルートにある `.env` に各種 API キー・認証情報を設定

## 実行方法

各サンプルを個別に実行して動作確認を行ってください:

```bash
python langchain_demo.py
```

```bash
python amazon_bedrock_integration.py
```

```bash
python vertex_ai_integration.py
```

---

各プラットフォームとの連携例を元に、さらに機能拡張を試みてください！


````
