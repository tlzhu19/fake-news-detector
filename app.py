import streamlit as st 
from joblib import load
import newspaper
import time 
import matplotlib.pyplot as plt


def read_article_url(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()

    return article.text


st.title('Fake News Detector')

loaded_text_clf = load('models/nb_model.joblib') 

st.subheader('Input text or give a url link to an article:')
article_url = st.text_input('Article URL: ')
article_text = st.text_area('Article Text: ', height=200)

if article_url:
    article_text = read_article_url(article_url)

display_input = st.checkbox('Display Input Text')
if display_input:
    st.write('Input text', article_text)


with st.spinner('Predicting...'):
    predicted = loaded_text_clf.predict([article_text])[0]
    probabilities = list(loaded_text_clf.predict_proba([article_text])[0])
    predicted_probability = probabilities[predicted]
    predicted_text = 'REAL' if predicted else 'FAKE'

if article_text:
    st.subheader('This article is {} with probability {:.2%}'.format(predicted_text, predicted_probability))
    plt.pie(probabilities, 
        labels=['Fake', 'Real'], 
        colors=['#e0a4a4', '#c0ffb5'], 
        autopct='%1.1f%%',
       )
    st.pyplot()



