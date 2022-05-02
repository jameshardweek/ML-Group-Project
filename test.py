import pandas as pd
import re

df = pd.read_csv('data/good_badnews_with_text.csv')
text = df['text']
y = df['label']

tweets = []

for tweet in text:
    tweets.append(re.sub(r'https?://\S+', '', tweet).strip().replace('#','').replace(',',''))

print()