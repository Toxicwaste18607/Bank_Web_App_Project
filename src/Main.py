import os
import streamlit as st 
import json
import random
from app_pages.miscellaneous import *
from app_pages.Dashboard import *
from app_pages.Transactions import *



#DEFS


   









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