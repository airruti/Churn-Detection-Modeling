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
combined_df['region'].loc[combined_df['Account Currency'] == 'USD'] = "NAM"
combined_df['region'].loc[combined_df['Account Currency'] == 'CAD'] = "NAM"
combined_df['region'].loc[combined_df['Account Currency'] == 'EUR'] = "EU"
combined_df['region'].loc[combined_df['Account Currency'] == 'GBP'] = "EU"
combined_df['region'].loc[combined_df['Account Currency'] == 'AUD'] = "AU"
combined_df['region'].loc[combined_df['Account Currency'] == 'NZD'] = "AU"
combined_df['region'].loc[combined_df['Account Currency'] == 'ZAR'] = "SA"

#Drop repeating columns/stuff we don't need
drop = ["placeholder", "Account Currency", "account_id", "Row Labels", "Full Account ID", "Max of Effective_Start_Date__c", "min_IO_seats_required", "Full User ID", "Account Record Type", "Type"]
combined_df.drop(columns=drop, inplace=True)

#Make it a CSV
combined_df.to_csv('combined.csv')

print(combined_df.head())

print("Done")