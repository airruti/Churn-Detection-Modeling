import pandas as pd
import streamlit as st

st.set_page_config( page_title="Churn Detection Modeling",
                    page_icon=":bar_chart:",
                    layout="wide")

df = pd.read_csv('combined.csv')

st.selectbox("Charts", ["Churn model", "Churn factors"])
st.dataframe(df)