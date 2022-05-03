import numpy as np
import pandas as pd
from joblib import dump, load
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm

df = pd.read_csv('data/twitter_processed.csv')

# tweets = [x for x in df['text']]
# y = [x for x in df['status']]

y = df['status']
X = df['text']

td = TfidfVectorizer()
X = td.fit_transform(X)

X_df = pd.DataFrame.sparse.from_spmatrix(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

old_clf = load('models/tfidf_svm')
old_y_pred = old_clf.predict(X_test)
old_score = accuracy_score(y_test, old_y_pred)

clf = svm.SVC()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

score = accuracy_score(y_test, y_pred)

classification_report = classification_report(y_test, y_pred)

print()
print(f'Old Accuracy: {old_score}')
print(f'New Accuracy: {accuracy_score(y_test, y_pred)}')
print()
print(f'Classification Report:')
print(f'======================================================')
print(f'{classification_report}')
print(f'======================================================')

if score > old_score:
    dump(clf, 'models/tfidf_svm')

# df = pd.DataFrame(X, columns = td.get_feature_names_out())

# test_sentence = 'man cured of disease'
# test_status = 1

# test_X = td.transform(test_sentence.split(' ')).toarray()

# test_predict = clf.predict(test_X)

# score = accuracy_score([test_status], test_predict)
