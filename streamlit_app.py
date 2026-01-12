
import streamlit as st
import pandas as pd

st.info("📘 누구나 볼 수 있도록 공개된 시트를 Pandas로 직접 불러오는 가장 간단한 방법입니다.\n📎 링크는 반드시 `export?format=csv` 형태로 설정하세요.")

csv_url1 = st.secrets["connections"]["gsheets"]["public_url"]
df1 = pd.read_csv(csv_url1)

# `choice` 항목을 카운트한 후 막대그래프로 표시합니다.
counts = df1["choice"].value_counts()
st.write("## `choice` 항목별 빈도수")
st.bar_chart(counts)
