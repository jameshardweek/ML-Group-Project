import pandas as pd
import re
import sklearn

df = pd.read_csv('data/good_badnews_with_text.csv')
text = df['text']
y = df['label']

tweets = []
words = set()

for tweet in text:
    tweet_text = re.sub(r'https?://\S+', '', tweet).strip()
    tweet_text = ''.join([x.lower() for x in tweet_text if x.isalpha() or x == ' '])
    tweets.append(tweet_text)
    tweet_words = [x.lower() for x in tweet_text.split(' ')]
    words = words.union(set(tweet_words))

print('Number of words in the corpus:',len(words))

print()