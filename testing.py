import pandas as pd
import streamlit as st
import altair as alt
from model import logisticReg
# from model import classReport
import seaborn as sns
from matplotlib import pyplot as plt

logisticReg("combined.csv")