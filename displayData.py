import pandas as pd
import streamlit as st

# streamlit run displayData.py 
st.set_page_config( page_title="Churn Detection Modeling",
                    page_icon=":bar_chart:",
                    layout="wide")

df = pd.read_csv('combined.csv')

churn_df = df

#churn_drop = ["Account ID",	"Full Account ID",	"Full User ID",	"Owner AMA / AUM",
	# "Connect 2021 from Opty	Connect 2021"	,"Connect 2020 from Opty",	"Connect 2020",
    # 	"Connect 2019",	"JUNO Account ID",	"Kaseya Market Segment",	"Auto Renewal Op Out",
    #     	"# of Closed Won Opportunities",	"Account Record Type",	"Type",	"Last Activity",
    #         	"Last Modified Date",	"Min of Effective_Start_Date__c",	"Max of Effective_End_Date__c",	"Max of Effective_Start_Date__c",
    #             	"Current State",	"account_user_id",	"reputation_to_date	created_at", "closed_at",
    #                 	"min_IO_seats_required",	"region"]
#churn_df.drop(columns=churn_drop, inplace=True)

st.header("Combined data set:")
st.selectbox("Charts", ["Churn model", "Churn factors"])
st.dataframe(df)
#st.bar_chart(churn_df)

# SIDEBAR
st.sidebar.header("Filters:")
region = st.sidebar.multiselect(
    "Select the region:",
    options=df['region'].unique(),
    default=df['region'].unique()
)
st.sidebar.caption("The regions consists of North America(NA), APAC(AU), and Europe(EU)")
ownerType = st.sidebar.multiselect(
    "Select the owner type:",
    options=df['Owner AMA / AUM'].unique(),
    default=df['Owner AMA / AUM'].unique()
)

df_selection = df.query(
    "region == @region"
)
