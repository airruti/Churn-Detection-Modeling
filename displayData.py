import pandas as pd
import streamlit as st
import altair as alt
import model
import seaborn as sns
from matplotlib import pyplot as plt
from PIL import Image
import statsmodels
from sklearn.ensemble import ExtraTreesClassifier




# streamlit run displayData.py
st.set_page_config(page_title="Churn Detection Modeling",
                   page_icon=Image.open('churnDetectionLogo.jpeg'),
                   layout="wide")

# image = Image.open('churnDetectionLogo.jpeg')
# st.image(image, width=50)

#df = pd.read_csv('combined.csv', low_memory=False)
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

main_df = pd.read_csv("combined.csv", low_memory=False)
drops = ["Kaseya Market Segment_- None -",
     "Kaseya Market Segment_End User", "Kaseya Market Segment_Financial Services", "Kaseya Market Segment_General Business",
      "Kaseya Market Segment_Government", "Kaseya Market Segment_Healthcare", "Kaseya Market Segment_Hospitality",
       "Kaseya Market Segment_Retail", "Kaseya Market Segment_Software Vendor", "Account Currency_AU",
        "Account Currency_SA", "reputation_to_date", "Connect 2019"]
main_df = main_df.drop(columns=drops)
# main body
st.header("Churn Detection Modeling")
st.selectbox("Charts", ["Churn model", "Churn factors"])
st.caption("First five values of the dataframe")
st.dataframe(main_df.head())
chart_data = main_df['Churn'].value_counts()

# For reference incase we want to change back to interactive bar graph
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
).properties(
    width=1000,
    height=700
)
st.altair_chart(c, use_container_width=True)

# For reference incase we want to switch back to matplotlib
# column_names = ['Churn_No', 'Churn_Yes']
# df2 = pd.DataFrame(columns = column_names)
# df2 = df2.append({'Churn_No': chart_data[0], 'Churn_Yes': chart_data[1]}, ignore_index=True)
# Churn = list(df2.keys())
# values = list(df2.values[0])
# fig = plt.figure(figsize = (15,5))
# plt.bar(Churn, values, color = ['blue', 'red'])
# plt.xlabel("Churn Detection")
# plt.ylabel("Number of Customers that Churn")
# plt.title("Determines how many customers were churned")
# st.pyplot(fig)



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

# st.markdown('### Logistic Regression Plots')
# binary_columns = [c for c in main_df.columns.values if sorted(list(main_df[c].value_counts().index)) == ([0, 1])]
# columns_regression_x = st.multiselect('Columns for the Y axis (dependent var): ', main_df.columns.values, default=None)
# columns_regression_y = st.multiselect('Columns for the X axis (independent vars): ', binary_columns, default=None)
# if columns_regression_x:
#     if columns_regression_y:
#         for x_axis in columns_regression_x:
#             for y_axis in columns_regression_y:
#                 fig = plt.figure(figsize=(20, 6))
#                 ax = sns.regplot(x=main_df[x_axis], y=main_df[y_axis], logistic=True, ci=0, line_kws={"color": "red"})
#                 ax.set_title("Logistic Regression Plot")
#                 ax.set_ylabel(y_axis.capitalize())
#                 ax.set_xlabel(x_axis.capitalize())
#                 st.pyplot(fig)

# st.markdown('### Feature Importance Graph')
# feature_importances = model.feature_imp("combined.csv").nlargest(10)
# my_colors= ['red', 'grey', 'blue', 'magenta', 'orange', 'green', 'purple', 'black']
# feature_importances.plot.barh(figsize = (30, 10), color = my_colors)
# plt.show()

st.markdown('### Feature Importance Graph')
one = pd.read_csv("combined.csv")
drops = ["Churn", "Kaseya Market Segment_- None -",
     "Kaseya Market Segment_End User", "Kaseya Market Segment_Financial Services", "Kaseya Market Segment_General Business",
      "Kaseya Market Segment_Government", "Kaseya Market Segment_Healthcare", "Kaseya Market Segment_Hospitality",
       "Kaseya Market Segment_Retail", "Kaseya Market Segment_Software Vendor", "Account Currency_AU",
        "Account Currency_SA", "reputation_to_date", "Connect 2019"]
y = one["Churn"]
x = one.drop(columns=drops)
s = ExtraTreesClassifier()
s.fit(x,y)
feature_importance = pd.Series(s.feature_importances_,index =x.columns)
my_colors= ['red', 'grey', 'blue', 'magenta', 'orange', 'green', 'purple', 'black']
fig = plt.subplots()
st.pyplot(feature_importance.plot.barh(color = my_colors, figsize = (15, 10)).figure)


two = model.k_fold("combined.csv")

st.markdown('### Confusion Matrix')
cf_matrix = two[1]
fig, ax = plt.subplots(figsize=(20,8))
ax = sns.heatmap(cf_matrix, annot=True, cmap='Blues', square=True)
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ')
ax.xaxis.set_ticklabels(['True','False'])
ax.yaxis.set_ticklabels(['True','False'])
st.pyplot(fig)

st.markdown('### Classification Report')
finalReport = two[0]
st.dataframe(finalReport)      


# For reference for interactive heatmap
# heatmap = alt.Chart(df3).mark_rect().encode(
#      alt.X('Var1:O', title = ''),
#      alt.Y('Var2:O', title = '', axis=alt.Axis(labelAngle=0)),
#      alt.Color('Corr:Q',
#                  scale=alt.Scale(scheme='viridis'))
# ).properties(title='Heat map of correlations of variables')
# st.altair_chart(heatmap, use_container_width=True)
