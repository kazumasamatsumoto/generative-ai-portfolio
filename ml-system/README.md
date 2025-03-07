# 機械学習システム

このモジュールは、テキスト分類タスクを通して機械学習モデルのトレーニングと評価の実装例を示します。
TF-IDF と Naive Bayes を用いたシンプルな例ですが、実際のデータセットに合わせた改良も可能です。

## 含まれる機能

- **train_model.py**
  テキストデータを用いて分類モデルの学習を実行
- **evaluate_model.py**
  学習済みモデルを用いて、テストデータに対する評価を実施

## 環境構築

1. 仮想環境をアクティベートする
2. ルートディレクトリで依存ライブラリをインストール
   ```bash
   pip install -r ../requirements.txt
   ```

## 実行方法

1. モデルの学習:
   ```bash
   python train_model.py
   ```
2. モデルの評価:
   ```bash
   python evaluate_model.py
   ```

---

シンプルな例から始め、実データに合わせた改良をぜひチャレンジしてください！
