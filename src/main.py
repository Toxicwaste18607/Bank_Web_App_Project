import os
import streamlit as st 
from pages import login from


APP_PATH = os.path.dirname(os.path.abspath(__file__))


def get_data_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(APP_PATH, "data", filename)



def check_user_exists():pass


class User():
    def __init__(self,username,role):
        self.username= username
        self.role=role







def hello_page(): 
    pass





#app code here


if "user" not in st.session_state:
    st.session_state.user=None
    login_page()

else:
    st.write("NOT IMPLEMENTED YET")