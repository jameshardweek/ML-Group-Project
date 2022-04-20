import pandas as pd
import json
import requests
from time import sleep, localtime, strftime

def current_time():
    return strftime("%H:%M:%S", localtime())

headers = {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAJQcbQEAAAAAIeIOC9LGcviZS5kjAwy8VeD7JSQ%3Dsdcfrz9iRwrwEzfhFqVygQmV5dsk4yY0K1hpwyP6ijPYJIFRyh"}

data = pd.read_table('good_badnews_no_text.tsv')
current_ids = pd.read_csv('new.csv')['id']
bad_ids = [int(x.replace("\n","")) for x in open('bad_ids', 'r').readlines()]

labels = {}
required_ids = []

for id, label in data.values:
    labels[id] = label
    if id not in current_ids.values and id not in bad_ids:
        required_ids.append(id)
    
for id in required_ids:
    print(f"[{current_time()}] Retrieving text for id: {id}")
    while True:
        tweet = requests.get(f"https://api.twitter.com/2/tweets/{id}", headers=headers)
        tweet_json = json.loads(tweet.content)
        try: 
            tweet_text = tweet_json['data']['text'].replace('\"','\'').replace('\n','').replace('\r','')
            print(f"[{current_time()}] Found text for {id}")
            with open('new.csv', 'a') as f:
                f.write(f"{id},\"{tweet_text}\",{labels[id]}\n")
            break
        except KeyError:
            try:
                if tweet_json['errors'][0]['title'] == 'Not Found Error' or tweet_json['errors'][0]['title'] == 'Authorization Error':
                    print(f"[{current_time()}] Bad id: {id}")
                    with open('bad_ids','a') as f:
                        f.write(f"{id}\n")
                    break
                else:
                    breakpoint()
            except KeyError:
                try:
                    if tweet_json['status'] == 429:
                        print(f"[{current_time()}] Too many requests, waiting 30 seconds...")
                        sleep(30)
                        continue
                    else:
                        breakpoint()
                except KeyError:
                    breakpoint()