import streamlit as st
from non_page_code.auth import *


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
                st.session_state.current_page ='home'
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











        


