import pandas as pd
import numpy as np
import sqlite3

subscription_df = pd.read_csv("JUNO - Subscriptions.csv")
sfdc_acc_export_df = pd.read_csv("JUNO - SFDC Account Export.csv")
product_data_df = pd.read_csv("JUNO - Cleaned Product Data - FINAL.csv")

combined_data = [subscription_df, sfdc_acc_export_df, product_data_df]

combined_df = pd.concat(combined_data)

connection_db = sqlite3.connect('combioned.db')

cursor = connection_db.cursor()

# cursor.execute("""
# CREATE TABLE Account_Export(
#    Account_ID                   VARCHAR(15) NOT NULL 
#   ,Full_Account_ID              VARCHAR(18) NOT NULL 
#   ,Full_User_ID                 VARCHAR(18) NOT NULL
#   ,Owner_AMA_AUM                VARCHAR(3)
#   ,Connect_2021_from_Opty       BIT  NOT NULL
#   ,Connect_2021                 BIT  NOT NULL
#   ,Connect_2020_from_Opty       INTEGER  NOT NULL
#   ,Connect_2020                 BIT  NOT NULL
#   ,Connect_2019                 BIT  NOT NULL
#   ,Account_Currency             VARCHAR(3) NOT NULL
#   ,JUNO_Account_ID              VARCHAR(16) NOT NULL
#   ,Kaseya_Market_Segment        VARCHAR(18)
#   ,Auto_Renewal_Op_Out          BIT  NOT NULL
#   ,_of_Closed_Won_Opportunities INTEGER  NOT NULL
#   ,Account_Record_Type          VARCHAR(27) NOT NULL
#   ,Type                         VARCHAR(15)
#   ,Last_Activity                VARCHAR(10)
#   ,Last_Modified_Date           DATE  NOT NULL
# );
# """)
# cursor.execute("""
# CREATE TABLE Subscriptions(
#    SBQQ_Account_c                 VARCHAR(18) NOT NULL FOREIGN KEY REFERENCES Account_Export(Full_Account_ID)
#   ,Effective_Start_Date_c         VARCHAR(19)
#   ,Effective_End_Date_c           VARCHAR(19)
#   ,SBQQ_SubscriptionEndDate_c     VARCHAR(19)
#   ,SBQQ_SubscriptionStartDate_c   VARCHAR(19)
#   ,SBQQ_TerminatedDate_c          VARCHAR(19)
#   ,SBQQ_BillingFrequency_c        VARCHAR(30)
#   ,SBQQ_ProductSubscriptionType_c VARCHAR(9)
# );
# """)
# cursor.execute("""
# CREATE TABLE Product_Data(
#    account_user_id       NUMERIC(15,9) NOT NULL
#   ,account_id            VARCHAR(16) NOT NULL
#   ,reputation_to_date    INTEGER 
#   ,created_at            VARCHAR(16) NOT NULL
#   ,closed_at             VARCHAR(16)
#   ,min_IO_seats_required INTEGER  NOT NULL
#   ,region                VARCHAR(2) NOT NULL

# );
# """)

cursor.execute("SELECT * FROM Account_Export")
