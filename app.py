import streamlit as st
import requests
from datetime import date
import json

API_KEY = "708ad74a333343d78c544425e5cb85cd"
DATE = date.today().strftime("%Y-%m-%d")

st.title("Good News Today")

headlines = requests.get(f"https://newsapi.org/v2/top-headlines?country=gb&apiKey={API_KEY}").content
headlines_json = json.loads(headlines)
articles = {}

def process_text(text):
    text = ''.join([x.lower() for x in text if x.isalpha() or x == ' '])
    return ' '.join([x for x in text.split()])

for article in headlines_json['articles']:
    # headline = article['title'].lower()
    # headline = ''.join([x for x in headline if x.isalpha() or x == ' '])
    articles[article['title']] = article['url']

for title, url in articles.items():
    st.write(f"[{title}]({url})")
    classify_text = process_text(title)
    print(classify_text)