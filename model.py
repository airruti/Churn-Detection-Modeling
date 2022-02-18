import pandas as pd
import numpy as np
import sqlite3

product_data_df = pd.read_csv("JUNO - Cleaned Product Data - FINAL.csv")
subscription_df = pd.read_csv("JUNO - Subscriptions.csv")
sfdc_acc_export_df = pd.read_csv("JUNO - SFDC Account Export.csv")

temp_df = sfdc_acc_export_df.merge(subscription_df, left_on='Full Account ID', right_on='Row Labels')
combined_df = temp_df.merge(product_data_df, left_on='JUNO Account ID', right_on='account_id')

combined_df.to_csv('combined.csv')

print(combined_df.head())