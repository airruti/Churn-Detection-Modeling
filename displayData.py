import pandas as pd
import streamlit as st

# streamlit run displayData.py 
st.set_page_config( page_title="Churn Detection Modeling",
                    page_icon=":bar_chart:",
                    layout="wide")

df = pd.read_csv('combined.csv')

st.header("Combined data set:")
st.dataframe(df)

# SIDEBAR
st.sidebar.header("Filters:")
region = st.sidebar.multiselect(
    "Select the region:",
    options=df['region'].unique(),
    default=df['region'].unique()
)
st.sidebar.caption("The regions consists of North America(NA), APAC(AU), and Europe(EU)")
ownerType = st.sidebar.multiselect(
    "Select the owner type:",
    options=df['Owner AMA / AUM'].unique(),
    default=df['Owner AMA / AUM'].unique()
)

df_selection = df.query(
    "region == @region"
)