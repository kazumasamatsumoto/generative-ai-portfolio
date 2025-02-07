# nlp-utils/text_preprocessing.py
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)

if __name__ == "__main__":
    sample_text = "This is a sample text, with numbers 123 and punctuation!"
    cleaned = clean_text(sample_text)
    no_stop = remove_stopwords(cleaned)
    print("Original:", sample_text)
    print("Cleaned:", cleaned)
    print("No Stopwords:", no_stop)
