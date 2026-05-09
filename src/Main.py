
import streamlit as st 
from app_pages.miscellaneous import *
from app_pages.Dashboard import *
from app_pages.Transactions import *
from non_page_code.core_code import app_core

st.set_page_config(layout="wide")



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
    st.session_state.current
    app_core()

    