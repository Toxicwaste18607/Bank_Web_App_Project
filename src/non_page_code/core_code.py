
import streamlit as st
from non_page_code.auth import *
from app_pages.Transactions import *






def app_core():
    user = st.session_state.user


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
        show_dashboard_page()

    if st.session_state.current_page =='deposit':
        deposit_page()

    if st.session_state.current_page == 'withdraw':
        withdrawal_page()