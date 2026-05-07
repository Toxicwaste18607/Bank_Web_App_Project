import streamlit as st
user=st.session_state.user

def show_transactions_page(user):
    st.title("Transactions")
    st.write(f"Transactions for {user.username}")




show_transactions_page(user)