# ml-system/train_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

def train_model():
    # ダミーデータセットの例
    data = {
        "text": [
            "I love this product", 
            "This is a bad product", 
            "Absolutely fantastic!", 
            "Not worth the price"
        ],
        "label": [1, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["text"])
    y = df["label"]
    model = MultinomialNB()
    model.fit(X, y)
    joblib.dump((vectorizer, model), "ml-system/text_classifier.pkl")
    print("モデルの学習が完了しました。")

if __name__ == "__main__":
    train_model()
