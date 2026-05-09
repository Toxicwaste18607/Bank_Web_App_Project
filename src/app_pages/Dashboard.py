import streamlit as st
from .Transactions import *



def show_dashboard_page():
    user = st.session_state.user
    st.session_state.current_page ='home'
    st.title("Dashboard")
    st.write(f"Welcome, {user.name}")

    st.write(f"Current Balance is ${user.balance:,.2f}")

    #if user.check == "user":
    with st.sidebar:
        st.write(f'Hello {user.name}.')
        if st.button('Home'):
            st.session_state.current_page='home'

        if st.button('Deposit'):
            st.session_state.current_page='deposit'

        if st.button('Withdraw'):
            st.session_state.current_page='withdraw'

        if st.button('Logout'):
            st.session_state.user = None
            st.rerun()

        if st.session_state.current_page == 'home':
            show_transactions_page()

        if st.session_state.current_page =='deposit':
            deposit_page()

        if st.session_state.current_page == 'withdraw':
            withdrawal_page()






