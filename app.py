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

# Load models
nb_model = load('models/MultinomialNB_model.joblib') 
lr_model = load('models/LogisticRegression_model.joblib') 

model_names = {
    'Multinomial Naive Bayes': nb_model, 
    'Logistic Regression': lr_model
}

# 1. Select Model
st.subheader('1. Select Model')
# list of possible models to run
model_to_run = st.selectbox(
    'Model to run: ',
    list(model_names.keys())
    )

loaded_text_clf = model_names[model_to_run]

# 2. Input article
st.subheader('2. Input text or give a url link to an article:')
article_url = st.text_input('Article URL: ')
article_text = st.text_area('Article Text: ', height=200)

# convert article url to text
if article_url:
    article_text = read_article_url(article_url)

# choice to display imported text
display_input = st.checkbox('Display Input Text')
if display_input:
    st.write('Input text', article_text)

# run prediction
with st.spinner('Predicting...'):
    predicted = loaded_text_clf.predict([article_text])[0]
    probabilities = list(loaded_text_clf.predict_proba([article_text])[0])
    predicted_probability = probabilities[predicted]
    predicted_text = 'REAL' if predicted else 'FAKE'

# return result
if article_text:
    st.subheader('This article is {} with probability {:.2%}'.format(predicted_text, predicted_probability))
    plt.pie(probabilities, 
        labels=['Fake', 'Real'], 
        colors=['#e0a4a4', '#c0ffb5'], 
        autopct='%1.1f%%',
       )
    st.pyplot()

st.markdown('_For source code see: https://github.com/tlzhu19/fake-news-detector_')

