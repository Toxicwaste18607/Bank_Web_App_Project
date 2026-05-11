
import streamlit as st
from non_page_code.auth import *
from app_pages.Transactions import *
from app_pages.Dashboard import *
from classes.user import User
from classes.admin import Admin
from app_pages.Transaction_History import show_transactions
from app_pages.Admin_view_user import admin_users_page






def app_core():
    user = st.session_state.user
    
    if st.session_state.current_page==None:
        st.session_state.current_page = 'home'


    if user.role== 'user':

        with st.sidebar:
            st.write(f'Hello {user.name}.')
            if st.button('Home'):
                st.session_state.current_page='home'

            if st.button('Deposit'):
                st.session_state.current_page='deposit'

            if st.button('Withdraw'):
                st.session_state.current_page='withdraw'

            if st.button("Histroy"):
                st.session_state.current_page='history'

            if st.button('Logout'):
                st.session_state.user= None
                st.session_state.current_page='home'
                st.rerun()
        


    if user.role=='admin':

        with st.sidebar:
            st.write(f'Admin screen')

            if st.button('Home'):
                st.session_state.current_page='home'

            if st.button('User Managment'):
                st.session_state.current_page='user'


            if st.button('Logout'):
                st.session_state.user= None
                st.session_state.current_page='home'

                st.rerun()
        







    if st.session_state.current_page == 'home':
        show_dashboard_page()

    if st.session_state.current_page =='deposit':
        deposit_page()

    if st.session_state.current_page == 'withdraw':
        withdrawal_page()

    if st.session_state.current_page=='history':
        show_transactions()



    if  st.session_state.current_page=='user': 
        admin_users_page()

