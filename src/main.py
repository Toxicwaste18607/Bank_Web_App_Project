import os
import streamlit as st 
import json



APP_PATH = os.path.dirname(os.path.abspath(__file__))


def get_data_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(APP_PATH, "data", filename)



def load_user_data():
    path= get_data_path("user_data")

    if not os.path.exists(path):
        return {}
    
    with open (path,'r') as file:
        return json.load(file)






def check_user_exists():pass


class User():
    def __init__(self,username,role):
        self.username= username
        self.role=role

#NONE INDEPENDENT PAGES

def login_page():
    st.header("Login Page")

    
    with st.form("login_form"):
        username=st.text_input("Enter your username")
        role = st.selectbox("Role", ["user", "admin"])
        submitted = st.form_submit_button("Login")

        if submitted:

            check_user_exists()

            st.session_state.user = User(username,role)
            st.success ("Logged in")
            st.rerun()


def hello_page(): 
    user = st.session_state.user
    st.write (f'Welcome {user.username} ')





#app code here


if "user" not in st.session_state:
    st.session_state.user=None
    login_page()

else:
    hello_page()