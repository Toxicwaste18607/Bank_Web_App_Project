import os
import streamlit as st 


APP_PATH = os.path.dirname(os.path.abspath(__file__))


def get_data_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(APP_PATH, "data", filename)

def login_page():
    st.header("Login Page")

    with st.form("login_form"):
        user_name=st.text_input("Enter your username")
        role = st.selectbox("Role", ["user", "admin"])
        submitted = st.form_submit_button("Login")

        if submitted:
            st.write(f"Hello {user_name} you are a {role}.")





#app code here

login_page()