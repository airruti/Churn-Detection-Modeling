import pandas as pd
import streamlit as st
import altair as alt
from model import logisticReg
import seaborn as sns
from matplotlib import pyplot as plt
from PIL import Image

# streamlit run displayData.py
st.set_page_config(page_title="Churn Detection Modeling",
                   page_icon=":bar_chart:",
                   layout="wide")

# Header and churn logo
st.header("Churn Detection Modeling")
image = Image.open('churnDetectionLogo.jpeg')
st.image(image, width=300)

df = pd.read_csv('display.csv')
# df.drop(columns="Unnamed: 0", inplace=True)

# SIDEBAR
# st.sidebar.header("Filters:")
# region = st.sidebar.multiselect(
#     "Select the region:",
#     options=df['region'].unique(),
#     default=df['region'].unique()
# )
# st.sidebar.caption("The regions consists of North America(NAM), APAC(AU), and Europe(EU)")
# ownerType = st.sidebar.multiselect(
#     "Select the owner type:",
#     options=df['Owner AMA / AUM'].unique(),
#     default=df['Owner AMA / AUM'].unique()
# )
# df = df.query(
#     "region == @region & `Owner AMA / AUM` == @ownerType"
# )


# main body
st.selectbox("Charts", ["Churn model", "Churn factors"])
# st.dataframe(df)
chart_data = df['Churn'].value_counts()

st.markdown('### Bar Graph')
column_names = ['Churn Categories', 'Number of Customers Churned']
df2 = pd.DataFrame(columns=column_names)
df2 = df2.append({'Churn Categories': 'Churn_No',
                 'Number of Customers Churned': chart_data[0]}, ignore_index=True)
df2 = df2.append({'Churn Categories': 'Churn_Yes',
                 'Number of Customers Churned': chart_data[1]}, ignore_index=True)
c = alt.Chart(df2).mark_bar().encode(
    alt.X('Churn Categories'),
    alt.Y('Number of Customers Churned'),
    alt.Color('Churn Categories'),
    alt.OpacityValue(0.7),
    tooltip=[alt.Tooltip('Churn Categories'),
             alt.Tooltip('Number of Customers Churned')]
).interactive().properties(
    width=1000,
    height=700
)
st.altair_chart(c, use_container_width=True)

main_df = pd.read_csv("combined.csv")
st.markdown('### Scatter Plots')
columns_scatter_x = st.multiselect("Columns for the X axis:", options=main_df.columns.values, default=None)
columns_scatter_y = st.multiselect("Columns for the Y axis:", options=main_df.columns.values, default=None)
if columns_scatter_x:
    if columns_scatter_y:
        for x_axis in columns_scatter_x:
            for y_axis in columns_scatter_y:
                fig = plt.figure(figsize=(20, 6))
                ax = sns.scatterplot(x=main_df[x_axis], y=main_df[y_axis])
                ax.set_title("Churn Relationship")
                ax.set_ylabel(y_axis.capitalize())
                ax.set_xlabel(x_axis.capitalize())
                st.pyplot(fig)

st.markdown('### Correlations heat map')
corrMatrix = main_df.corr()
fig = plt.figure(figsize=(30, 10))
ax = sns.heatmap(corrMatrix, annot=True)
ax.set_title('Heat map of correlations of variables')
st.pyplot(fig)

st.markdown('### Logistic Regression Plots')
binary_columns = [c for c in main_df.columns.values if sorted(list(main_df[c].value_counts().index)) == ([0, 1])]
columns_regression_x = st.multiselect('Columns for the X axis: ', main_df.columns.values, default=None)
columns_regression_y = st.multiselect('Columns for the Y axis: ', binary_columns, default=None)
if columns_regression_x:
    if columns_regression_y:
        for x_axis in columns_regression_x:
            for y_axis in columns_regression_y:
                fig = plt.figure(figsize=(20, 6))
                ax = sns.regplot(x=main_df[x_axis], y=main_df[y_axis], logistic=True, ci=0, line_kws={"color": "red"})
                ax.set_title("Logistic Regression Plot")
                ax.set_ylabel(y_axis.capitalize())
                ax.set_xlabel(x_axis.capitalize())
                st.pyplot(fig)

st.markdown('### Classification Report')
finalReport = logisticReg("combined.csv")
st.dataframe(finalReport)             

             

# For reference for interactive heatmap
# heatmap = alt.Chart(df3).mark_rect().encode(
#      alt.X('Var1:O', title = ''),
#      alt.Y('Var2:O', title = '', axis=alt.Axis(labelAngle=0)),
#      alt.Color('Corr:Q',
#                  scale=alt.Scale(scheme='viridis'))
# ).properties(title='Heat map of correlations of variables')
# st.altair_chart(heatmap, use_container_width=True)
