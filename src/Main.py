
import streamlit as st 
from app_pages.miscellaneous import *
from app_pages.Dashboard import *
from app_pages.Transactions import *





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
    show_dashboard_page()

    