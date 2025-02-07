# ml-system/evaluate_model.py
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

def evaluate_model():
    vectorizer, model = joblib.load("ml-system/text_classifier.pkl")
    # ダミーテストデータの例
    data = {
        "text": [
            "I really like it", 
            "Terrible experience"
        ],
        "label": [1, 0]
    }
    df = pd.DataFrame(data)
    X_test = vectorizer.transform(df["text"])
    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(df["label"], predictions))
    print("Classification Report:")
    print(classification_report(df["label"], predictions))

if __name__ == "__main__":
    evaluate_model()
