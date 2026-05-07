import streamlit as st




def withdrawal():pass

def deposit():pass


def show_transactions_page():
    
    choice = st.radio ("Choose", ["Withdrawal","Deposit"])
    if choice == "Withdrawal":
        withdrawal()
    if choice== "Deposit":
        deposit()







