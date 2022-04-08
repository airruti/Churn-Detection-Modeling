from re import X
import pandas as pd
import streamlit as st
# import altair as alt
# from model import logisticReg
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['figure.figsize'] = 1,1

main_df = pd.read_csv("combined.csv")
binary_columns = [c for c in main_df.columns.values if sorted(list(main_df[c].value_counts().index)) == ([0, 1])]

st.markdown('### Logistic Regression: Duration vs. Churn outcome')
fig = plt.figure(figsize=(10, 10))
x = main_df['Duration']
y = main_df['Churn']
ax = sns.regplot(x=x, y=y, data=main_df, logistic=True, ci=None, line_kws={"color": "red"})
ax.set_title("Logistic Regression Plot")
ax.set_ylabel('test')
ax.set_xlabel('test')
ax.set_xlim(1,4000)
st.pyplot(fig)

max = 0
#Loop through the array    
for i in range(0, x.unique().size):    
    #Compare elements of array with max    
   if(x.unique()[i] > max):    
       max = x.unique()[i];    
print("Largest element: " + str(max));   