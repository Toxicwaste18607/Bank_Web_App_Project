import streamlit as st
user=st.session_state.user


if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please log in first.")
    st.stop()


def show_transactions_page():
    user = st.session_state.user

    st.title("Transactions")
    st.write(f"Transactions for {user.name}")




show_transactions_page()