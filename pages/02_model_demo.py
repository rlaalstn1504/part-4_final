import streamlit as st
from src.model import predict_texts
import pandas as pd

st.header("텍스트 분류 예측 데모")

texts = st.text_area("문장 입력 (줄바꿈으로 여러 문장 가능)", "good\nbad\nawesome")

if st.button("예측 실행"):
    try:
        input_list = [t for t in texts.split("\n") if t.strip()]
        result_df = predict_texts(input_list)

        st.success("예측 완료 ")
        st.dataframe(result_df)

        st.bar_chart(result_df.set_index("text")["prob"])

        # 로그 저장
        result_df.to_csv("data/log.csv", mode="a", index=False, header=False)
    except Exception as e:
        st.error(f"예측 중 오류 발생: {e}")