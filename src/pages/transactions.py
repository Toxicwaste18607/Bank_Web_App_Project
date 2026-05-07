import streamlit as st

def show_transactions_page(user):
    st.title("Transactions")
    st.write(f"Transactions for {user.username}")




show_transactions_page(user)