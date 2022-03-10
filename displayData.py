import pandas as pd
import streamlit as st
import altair as alt

# streamlit run displayData.py 
st.set_page_config( page_title="Churn Detection Modeling",
                    page_icon=":bar_chart:",
                    layout="wide")

df = pd.read_csv('combined.csv', nrows=1000)
df.drop(columns="Unnamed: 0", inplace=True)

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
df = df.query(
    "region == @region & `Owner AMA / AUM` == @ownerType"
)
# main body
st.header("Combined data set:")
st.selectbox("Charts", ["Churn model", "Churn factors"])
st.dataframe(df)
chart_data = df['Churn'].value_counts()
#st.bar_chart(chart_data)
column_names = ['Churn Categories', 'Number of Customers Churned']
df2 = pd.DataFrame(columns = column_names)
df2 = df2.append({'Churn Categories': 'Churn_No', 'Number of Customers Churned': chart_data[0]}, ignore_index=True)
df2 = df2.append({'Churn Categories': 'Churn_Yes', 'Number of Customers Churned': chart_data[1]}, ignore_index=True)
c = alt.Chart(df2).mark_bar().encode(
    alt.X('Churn Categories'),
    alt.Y('Number of Customers Churned'),
    alt.Color('Churn Categories'),
    alt.OpacityValue(0.7),
    tooltip = [alt.Tooltip('Churn Categories'),
               alt.Tooltip('Number of Customers Churned')]
).interactive()
st.altair_chart(c, use_container_width=True)