import os
import streamlit as st 
import json
import random
from app_pages.miscellaneous import *
from app_pages.Dashboard import *
from app_pages.Transactions import *


APP_PATH = os.path.dirname(os.path.abspath(__file__))

#DEFS

def check_login(user_id, password):
    users = load_user_data()

    if user_id in users:
        user_data = users[user_id]

        if user_data["password"] == password:
            return User(
                user_id=user_id,
                name=user_data["name"],
                role=user_data["role"],
                balance=user_data["balance"],
                email=user_data["email"]
            )

    return None
   









#app code here

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    choice = st.radio("Choose", ["Login", "Create Account"])

    if choice == "Login":
        login_page()
    else:
        create_new_account()

else:
    hello_page()

    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()