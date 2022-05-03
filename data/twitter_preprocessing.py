import re

import pandas as pd

df = pd.read_csv('data/twitter_unprocessed.csv')

data = {}
for i, id in enumerate(df['id']):
    text = re.sub(r'https?://\S+', '', df.iloc[i]['text']).strip()
    text = ''.join([x.lower() for x in text if x.isalpha() or x == ' '])
    text= ' '.join([x for x in text.split()])
    status = df.iloc[i]['label']
    data[id] = {
        'text': text,
        'status': status
    }

new_df = pd.DataFrame().from_dict(data, orient='index', columns=['text', 'status'])

new_df.to_csv(index_label='id', path_or_buf='processed_twitter.csv')
