import streamlit as st

columns = st.columns(2)

col1=columns[0]
col2=columns[1]


def withdrawal():pass

def deposit():pass


def show_transactions_page():
    
    choice = st.radio ("Choose", ["Withdrawal","Deposit"])
    if choice == "Withdrawal":
        withdrawal()
    if choice== "Deposit":
        deposit()







