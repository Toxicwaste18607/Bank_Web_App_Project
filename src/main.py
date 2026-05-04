import os
import streamlit as st 


APP_PATH = os.path.dirname(os.path.abspath(__file__))


def get_data_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(APP_PATH, "data", filename)

class User():
    def __init__(self,username,role):
        self.username= username
        self.role=role



def login_page():
    st.header("Login Page")

    
    with st.form("login_form"):
        username=st.text_input("Enter your username")
        role = st.selectbox("Role", ["user", "admin"])
        submitted = st.form_submit_button("Login")

        if submitted:
            st.session_state.user = User(username,role)
            st.success ("Logged in")
            st.rerun()


def hello_page(): 
    pass





#app code here


if "user" not in st.session_state:
    st.session_state.user=None
    login_page()

else:
    st.write("NOT IMPLEMENTED YET")