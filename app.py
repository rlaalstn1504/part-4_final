import streamlit as st
import pandas as pd
import time

@st.cache_data
def load_large_csv():
    time.sleep(3)  # 로드 지연 시뮬레이션
    df = pd.DataFrame({"A": range(1000), "B": range(1000, 2000)})
    return df

st.header("📁 캐싱 데이터 로드 테스트")

t0 = time.perf_counter()
df = load_large_csv()
dt = time.perf_counter() - t0

st.write(f"로드 시간: {dt:.2f}초")
st.dataframe(df.head())