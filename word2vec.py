from gensim.models import Word2Vec
from gensim.test.utils import common_texts
import pandas as pd
import gensim.downloader as gensim_api
import nltk 
from sklearn.pipeline import Pipeline
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from nltk.corpus import stopwords
import numpy as np

df = pd.read_csv('data/twitter_processed.csv')
X = [x for x in df['text']]
y = [y for y in df['status']]

nltk.download('stopwords')
stop_words=set(stopwords.words('english'))

lines_without_stopwords=[]
#stop words contain the set of stop words
for line in X:
    lines_without_stopwords.append([x for x in line.split() if x not in stop_words])

X=lines_without_stopwords

nlp = gensim_api.load("word2vec-google-news-300")
# nlp = gensim_api.load("text8")

X_vectors = []
for line in X:
    mean = np.mean([nlp[x] for x in line if x in nlp])
    if np.isnan(mean):
        X_vectors.append(0)
    else:
        X_vectors.append(mean)
X_vectors = np.array(X_vectors).reshape(-1,1)
# X_vectors.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X_vectors, y, test_size=0.3, random_state=0)

clf = svm.SVC()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
# confusion_matrix(y_test, y_pred)