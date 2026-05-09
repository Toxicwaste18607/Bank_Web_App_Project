import streamlit as st
from .Transactions import *



def show_dashboard_page():
    user = st.session_state.user

    st.title("Dashboard")
    st.write(f"Welcome, {user.name}")

    st.write(f"Current Balance is ${user.balance:,.2f}")

    #if user.check == "user":
    with st.sidebar:
        st.write(f'Hello {user.name}.')
        if st.button('Home'):pass

        if st.button('Deposit'):pass

        if st.button('Withdraw'):pass

        if st.buttom('Logout'):
            st.session_state.user = None
            st.rerun()







