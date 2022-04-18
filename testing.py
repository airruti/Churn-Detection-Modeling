import pandas as pd

df = pd.read_csv("combined.csv", low_memory=False)

df['region'].unique()

# None, Channel,Education,End User,Financial Services,General Business,Government,Healthcare,Hospitality,MSP,Retail, Software Vendor
# Account Currency_AU,Account Currency_EU,Account Currency_NAM,Account Currency_SA"