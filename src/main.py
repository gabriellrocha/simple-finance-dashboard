import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

st.set_page_config(page_title="Simple Finance App", page_icon="💰", layout="wide")

def load_transactions(file) -> pd.DataFrame:
    try:
        df = pd.read_csv(file)
        df["Amount"] = df["Amount"].str.replace(",", "").astype(float)
        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y")
        st.dataframe(df, hide_index=True )
        return df
    
    except Exception as e:
        st.error(f"Error process file: {str(e)}")


def main():
    st.title("Simple Finance Dashboard")

    uploaded_file = st.file_uploader("Upload your transaction CSV file", type=["csv"])

    if uploaded_file is not None:

        df = load_transactions(uploaded_file)

        if df is not None:
        
            debits_df = df[df["Debit/Credit"] == "Debit"].copy()
            credits_df = df[df["Debit/Credit"] == "Credit"].copy()

            tab1, tab2 = st.tabs(["Expenses (Debits)", "Payments (Credits)"])

            with tab1:
                st.dataframe(debits_df, hide_index=True)

            with tab2:
                st.dataframe(credits_df, hide_index=True)

main()