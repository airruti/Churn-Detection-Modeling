# created for the sole purpose of analyzing/filter data

import pandas as pd
import numpy as np

combined = pd.read_csv("combined.csv", low_memory=False)
cleaned = pd.read_csv("JUNO - Cleaned Product Data - FINAL.csv", low_memory=False)
account = pd.read_csv("JUNO - SFDC Account Export.csv", low_memory=False)
subs = pd.read_csv("JUNO - Subscriptions.csv", low_memory=False)

print(cleaned['region'].unique())