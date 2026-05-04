import os
import streamlit as st 

import streamlit as st

st.write("Not Implemented Yet")


def login_page():
    st.header("Login Page")

    
    with st.form("login_form"):
        username=st.text_input("Enter your username")
        role = st.selectbox("Role", ["user", "admin"])
        submitted = st.form_submit_button("Login")

        if submitted:
            st.session_state_state.user = User(username,role)
            st.success ("Logged in")
            st.rerun
