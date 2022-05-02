import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

tweets = [x for x in pd.read_csv('data/processed.csv')['text']]
y = [x for x in pd.read_csv('data/processed.csv')['status']]

td  = TfidfVectorizer()
X = td.fit_transform(tweets).toarray()

feature_names = [x for x in td.get_feature_names_out()]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

classifier = MultinomialNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

classification_report = classification_report(y_test, y_pred)

print()
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print()
print(f'Classification Report:')
print(f'======================================================')
print(f'{classification_report}')
print(f'======================================================')