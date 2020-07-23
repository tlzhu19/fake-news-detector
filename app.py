import streamlit as st 
from joblib import load
import newspaper


def read_article_url(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()

    return article.text


st.title('Fake News Detector')

loaded_text_clf = load('models/nb_model.joblib') 

st.subheader('Input text or give a url link to an article:')
article_url = st.text_input('Article URL: ')
article_text = st.text_input('Article Text: ')

if article_url:
    article_text = read_article_url(article_url)

display_input = st.checkbox('Display Input Text')
if display_input:
    st.write('Input text', article_text)


predicted = loaded_text_clf.predict([article_text])
predicted_prob = loaded_text_clf.predict_proba([article_text])[0][predicted][0]
predicted_text = 'REAL' if predicted else 'FAKE'
st.subheader('This article is {} with probability {:.2%}'.format(predicted_text, predicted_prob))



