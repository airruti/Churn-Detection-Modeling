import pandas as pd
# import streamlit as st
# import altair as alt
# from model import logisticReg
# import seaborn as sns
# from matplotlib import pyplot as plt

main_df = pd.read_csv("combined.csv")
binary_columns = [c for c in main_df.columns.values if sorted(list(main_df[c].value_counts().index)) == ([0, 1])]
print(binary_columns)