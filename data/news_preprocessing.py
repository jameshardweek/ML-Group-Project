import re

import pandas as pd

df = pd.read_csv('data/news_unprocessed.csv')

data = {}
for i, id in enumerate(df['URL']):
    text = ''.join([x.lower() for x in df.iloc[i]['Title'] if x.isalpha() or x == ' '])
    text= ' '.join([x for x in text.split()])
    status = df.iloc[i]['Majority Score']
    if status == 2:
        status = 1
    elif status == 3:
        status = 0
    data[id] = {
        'text': text,
        'status': status
    }

new_df = pd.DataFrame().from_dict(data, orient='index', columns=['status', 'text'])

new_df.to_csv(index_label='URL', path_or_buf='news_processed.csv')
