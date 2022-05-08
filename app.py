import json
from datetime import date

import iso3166
import requests
import streamlit as st
from joblib import load

API_KEY = "708ad74a333343d78c544425e5cb85cd"
DATE = date.today().strftime("%Y-%m-%d")
country = 'gb'

ip_info = requests.get('http://ipinfo.io/json').content
ip_info_json = json.loads(ip_info)
current_country = ip_info_json['country'].lower()

if current_country in iso3166.countries:
    country = current_country

st.title("Good News Today")

headlines = requests.get(f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}").content
headlines_json = json.loads(headlines)
articles = {}

def process_text(text):
    text = ''.join([x.lower() for x in text if x.isalpha() or x == ' '])
    return ' '.join([x for x in text.split()])

for article in headlines_json['articles']:
    title = ''.join(article['title'].split(' - ')[:-1])
    articles[title] = article['url']

clf = load('models/svm_both')
td = load('models/td_both')

# st.write([f"{x}" for x in articles.keys()])

for title, url in articles.items():
    clean_title = process_text(title)
    clean_title = ' '.join([x for x in process_text(title).split(' ') if x in td.get_feature_names_out()])
    # print(clean_title)
    X = td.transform([clean_title])
    prediction = clf.predict(X)[0]

    if prediction == 1:
        st.write(f"[{title}]({url})")