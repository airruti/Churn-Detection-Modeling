import pandas as pd
import streamlit as st
import altair as alt
from model import logisticReg
# from model import classReport
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('display.csv', nrows=1000)


options=df['Account Record Type'].unique()
print(options)
options=df['Owner AMA / AUM'].unique()
print(options)
options=df['Account Currency'].unique()
print(options)
options=df['Kaseya Market Segment'].unique()
print(options)
options=df['Type'].unique()
print(options)
options=df['Churn'].unique()
print(options)
options=df['Current State'].unique()
print(options)