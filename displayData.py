import pandas as pd
import streamlit as st

st.set_page_config( page_title="Churn Detection Modeling",
                    page_icon=":bar_chart:",
                    layout="wide")

df = pd.read_csv('combined.csv')

st.dataframe(df)