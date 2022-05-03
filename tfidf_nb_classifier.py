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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

clf = MultinomialNB()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

classification_report = classification_report(y_test, y_pred)

print()
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print()
print(f'Classification Report:')
print(f'======================================================')
print(f'{classification_report}')
print(f'======================================================')


df = pd.DataFrame(X, columns = td.get_feature_names_out())

test_sentence = 'man cured of disease'
test_status = 1

test_X = td.transform(test_sentence.split(' ')).toarray()

test_predict = clf.predict(test_X)

score = accuracy_score([test_status], test_predict)