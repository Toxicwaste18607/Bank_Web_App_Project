import streamlit as st
from non_page_code.auth import *
from .Transactions import *


def search_username():
    pass 


def login_page():
    with st.form("login_form"):
        user_info = st.text_input("Enter your user ID or Username.")

        password = st.text_input(
            "Enter your password",type="password" )

        submitted = st.form_submit_button("Login")

        if submitted:
            user = check_login(user_info, password)

            if user is not None:
                st.session_state.user = user
                st.success("Logged in!")
                st.rerun()

            else:
                st.error("Invalid login")


def create_new_account(): 
    st.header("New User")

    with st.form("new_user_form"):
        username=st.text_input("Please enter a Username")
        name = st.text_input("Enter your name")
        password = st.text_input("Enter a password", type="password")
        email = st.text_input("Email")

        submitted = st.form_submit_button("Create Account")

        if submitted:
            if name == "" or password =="" or email=="" or username=="":
                st.error("Please fill out all feilds")
            
            else:
                new_id = create_user(password, name,username, email)
                st.success(f"Account created! Your user ID is {new_id}")



def show_dashboard_page():


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







        


