import streamlit as st
import pandas as pd
import numpy as np

st.title("컴포넌트 카탈로그")

# 입력 위젯
st.subheader("입력 위젯 예제")
if "user" not in st.session_state:
    st.session_state.user = ""

name = st.text_input("이름 입력", st.session_state.user)
st.session_state.user = name
level = st.slider("숙련도", 1, 10, 5)
lang = st.selectbox("언어 선택", ["Python", "Java", "C++"])
file = st.file_uploader("CSV 업로드")

# 출력 요소
st.subheader("출력 요소 예제")
st.write("텍스트 출력 예시:", name)
st.json({"name": name, "level": level, "lang": lang})

data = pd.DataFrame({
    "x": np.arange(1, 6),
    "y": np.random.randint(10, 100, 5)
})
st.bar_chart(data.set_index("x"))

# 상태 관리
st.subheader("Session State 예제")
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("카운터 증가"):
    st.session_state.counter += 1

st.write("현재 카운트:", st.session_state.counter)