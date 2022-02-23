import pandas as pd
import numpy as np
import sqlite3

#Read CSV files
product_data_df = pd.read_csv("JUNO - Cleaned Product Data - FINAL.csv")
subscription_df = pd.read_csv("JUNO - Subscriptions.csv")
sfdc_acc_export_df = pd.read_csv("JUNO - SFDC Account Export.csv")

#Merge data
temp_df = sfdc_acc_export_df.merge(subscription_df, left_on='Full Account ID', right_on='Row Labels')
combined_df = temp_df.merge(product_data_df, left_on='JUNO Account ID', right_on='account_id')

#Drop repeating columns/stuff we don't need
drop = ["placeholder", "account_id", "Row Labels"]
combined_df.drop(columns=drop, inplace=True)

#This will fill the "region" column not sure why it messes up 
#when we do the merge... but we might want to use region for our model
combined_df['region'].loc[combined_df['Account Currency'] == 'USD'] = "NA"
combined_df['region'].loc[combined_df['Account Currency'] == 'CAD'] = "NA"
combined_df['region'].loc[combined_df['Account Currency'] == 'EUR'] = "EU"
combined_df['region'].loc[combined_df['Account Currency'] == 'GBP'] = "EU"
combined_df['region'].loc[combined_df['Account Currency'] == 'AUD'] = "AU"
combined_df['region'].loc[combined_df['Account Currency'] == 'NZD'] = "AU"
combined_df['region'].loc[combined_df['Account Currency'] == 'ZAR'] = "SA"

#Make it a CSV
combined_df.to_csv('combined.csv')

print("Done")