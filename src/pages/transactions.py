import streamlit as st
user=st.session_state.user


if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please log in first.")
    st.stop()


def withdrawal():pass

def deposit():pass


def show_transactions_page():
    user = st.session_state.user

    st.title("Transactions")
    choice = st.radio ("Choose", ["Withdrawal","Deposit"])
    if choice == "Withdrawal":
        withdrawal()
    if choice== "Deposit":
        deposit()







show_transactions_page()