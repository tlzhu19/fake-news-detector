# Fake News Detector

## 0. About
Create app to detect fake news.

https://fake-news-detector-tz.herokuapp.com/

### Files
* **models/**:  scikit-learn models trained in _analysis.ipynb_
* **analysis.ipynb**: trains model
* **app.py**: Streamlit app
* **requirements.txt**: Python library versions needed to run app

## 1. Dataset
https://www.kaggle.com/jruvika/fake-news-detection

## 2. Requirements

### 2.1 Kaggle API
This requires using the python Kaggle API to download the dataset. [Steps to set up Kaggle API](https://www.kaggle.com/c/two-sigma-financial-news/discussion/83593):
1. `pip install kaggle`
2. `cd ~/.kaggle`
3. Go to www.kaggle.com -> Your Account -> Create New API token
4. `mv ~/Downloads/kaggle.json ./`
5. `chmod 600 ./kaggle.json`

### 2.2 Streamlit
The app uses [Streamlit](https://docs.streamlit.io/en/stable/getting_started.html)

To run app locally, you should have Streamlit installed.
```
>> pip install streamlit
```
Then,
```
>> streamlit run app.py
```
