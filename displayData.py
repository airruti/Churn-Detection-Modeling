import pandas as pd
import streamlit as st
import altair as alt

# streamlit run displayData.py 
st.set_page_config( page_title="Churn Detection Modeling",
                    page_icon=":bar_chart:",
                    layout="wide")

df = pd.read_csv('combined.csv')

df.drop(columns="Unnamed: 0", inplace=True)

st.header("Combined data set:")
st.selectbox("Charts", ["Churn model", "Churn factors"])
st.dataframe(df)
st.bar_chart(df['Churn'].value_counts())

# SIDEBAR
st.sidebar.header("Filters:")
region = st.sidebar.multiselect(
    "Select the region:",
    options=df['region'].unique(),
    default=df['region'].unique()
)
st.sidebar.caption("The regions consists of North America(NAM), APAC(AU), and Europe(EU)")
ownerType = st.sidebar.multiselect(
    "Select the owner type:",
    options=df['Owner AMA / AUM'].unique(),
    default=df['Owner AMA / AUM'].unique()
)

df_selection = df.query(
    "region == @region"
)
