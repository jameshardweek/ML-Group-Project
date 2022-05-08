import math
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn import svm
from joblib import load, dump
from geotext import GeoText
from sklearn.neighbors import KNeighborsClassifier

def main():
    # twitter_df = pd.read_csv('data/twitter_processed.csv')
    # twitter_text = twitter_df['text']
    # twitter_labels = twitter_df['status']

    # news_df = pd.read_csv('data/news_processed.csv')
    # news_text = news_df['text']
    # news_labels = news_df['status']

    # all_text = twitter_text.append(news_text)
    # y = twitter_labels.append(news_labels)

    df = pd.read_csv('data/all_processed.csv')
    text = df['text']
    y = df['status']

    td = TfidfVectorizer()
    X = td.fit_transform(text)

    X_df = pd.DataFrame.sparse.from_spmatrix(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=0)

    n = int(math.sqrt(len(text)))

    # clf = svm.SVC()
    clf = KNeighborsClassifier(n_neighbors=5)
    clf.fit(X_train, y_train)

    # old_clf = load('models/svm_both')

    y_pred = clf.predict(X_test)
    # old_pred = old_clf.predict(X_test)

    clf_report = classification_report(y_test, y_pred)

    clf_score = accuracy_score(y_test, y_pred)
    # old_score = accuracy_score(y_test, old_pred)

    print()
    print(f'Accuracy: {clf_score}')
    print()
    print(f'Classification Report:')
    print(f'======================================================')
    print(f'{clf_report}')
    print(f'======================================================')

    # if clf_score > old_score:
    #     dump(clf, 'models/svm_both')
    #     print(f"new score found, saving classifier")

    # text = [process_text(x) for x in all_text]
    # labels = [[x] for x in y]

    # text = process_text("London, jinae aomsad amsterdam Africa")

    # dictionary = dict(zip(text, labels))

    # output_df = pd.DataFrame.from_dict(dictionary, orient='index', columns=['status']).to_csv('data/all_processed.csv', columns =['status'], index_label='text')

    # main()

def process_text(text):
    text = ''.join([x.lower() for x in text if x.isalpha() or x == ' '])
    return ' '.join([x for x in text.split()])

if __name__ == '__main__':
    main()
