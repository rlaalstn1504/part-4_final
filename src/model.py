import streamlit as st
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

@st.cache_resource
def load_model():
    """더미 텍스트 분류 모델 로드"""
    X = ["good", "great", "awesome", "bad", "awful", "terrible"]
    y = [1, 1, 1, 0, 0, 0]
    model = Pipeline([
        ("vec", CountVectorizer()),
        ("clf", LogisticRegression(max_iter=200))
    ])
    model.fit(X, y)
    return model

@st.cache_data
def predict_texts(texts):
    """입력 텍스트 리스트 예측"""
    model = load_model()
    preds = model.predict(texts)
    probs = model.predict_proba(texts)[:, 1]
    df = pd.DataFrame({"text": texts, "label": preds, "prob": probs})
    return df