import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import warnings

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=FutureWarning)

nltk.download('stopwords')
nltk.download('wordnet')

df = pd.read_csv(r'C:\Users\Пользователь\Downloads\Telegram Desktop\new_reviews2.csv')

def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    stop_words = set(stopwords.words('russian'))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

df['review'] = df['review'].apply(preprocess_text)

X = df['review']
y = df['review_mark']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X_train_text = vectorizer.fit_transform(X_train)
X_test_text = vectorizer.transform(X_test)

param_grid = {
    'C': [0.02, 0.2, 2, 11, 100],
    'solver': ['lbfgs', 'liblinear']
}
grid = GridSearchCV(LogisticRegression(max_iter=1000, multi_class='multinomial'), param_grid, cv=5, scoring='accuracy')
grid.fit(X_train_text, y_train)

best_params = grid.best_params_
print("Лучшие параметры: ", best_params)

model = LogisticRegression(multi_class='multinomial', solver=best_params['solver'], C=best_params['C'], max_iter=1000)
model.fit(X_train_text, y_train)

y_pred = model.predict(X_test_text)

print("Accuracy on test data: {:.2f}%".format(accuracy_score(y_test, y_pred) * 100))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

