import pandas as pd
import numpy as np

#Read CSV files
product_data_df = pd.read_csv("JUNO - Cleaned Product Data - FINAL.csv")
subscription_df = pd.read_csv("JUNO - Subscriptions.csv")
sfdc_acc_export_df = pd.read_csv("JUNO - SFDC Account Export.csv")

#Merge data
temp_df = sfdc_acc_export_df.merge(subscription_df, left_on='Full Account ID', right_on='Row Labels')
combined_df = temp_df.merge(product_data_df, left_on='JUNO Account ID', right_on='account_id')

#This will fill the "region" column not sure why it messes up 
#when we do the merge... but we might want to use region for our model
account_currency_map = {'USD': 'NAM', 'CAD': 'NAM', 'EUR': 'EU', 'GBP': 'EU', 'AUD': 'AU', 'NZD': 'AU', 'ZAR': 'SA'}
combined_df['Account Currency'] = combined_df['Account Currency'].map(account_currency_map)

#csv for diplaydata for UI
combined_df.to_csv("display.csv")

##todo: 
"""
Calculate Churn within Python
Data cleaning
"""

#Drop repeating columns/stuff we don't need
drop = ["Account ID", "Full User ID", "JUNO Account ID", "Row Labels", "Full Account ID",  "account_id", "account_user_id", "Current State", "created_at", "Last Activity", "Last Modified Date", "closed_at", "Min of Effective_Start_Date__c", "Owner AMA / AUM", "Max of Effective_End_Date__c", "Account Currency",  "Max of Effective_Start_Date__c", "min_IO_seats_required",  "Account Record Type", "Type"]
combined_df.drop(columns=drop, inplace=True)

#make indicator variables
combined_df = pd.get_dummies(combined_df, columns=["Kaseya Market Segment", "region"])

#remove invalid durations due to faulty data
combined_df = combined_df[combined_df['Duration'] != '#NUM!']
combined_df = combined_df.dropna(how='any')

#Make it a CSV
combined_df.to_csv('combined.csv', index=False)

print(combined_df.head())

print("Done")