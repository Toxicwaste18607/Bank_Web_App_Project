import os
import streamlit as st 
import json
import random
from app_pages.miscellaneous import *
from app_pages.Dashboard import *
from app_pages.Transactions import *


APP_PATH = os.path.dirname(os.path.abspath(__file__))

#DEFS
def get_data_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(APP_PATH, "data", filename)


def load_user_data():
    path= get_data_path("user_data.json")

    if not os.path.exists(path):
        return {}
    
    with open (path,'r') as file:
        return json.load(file)
    '''Loads user data from the file'''


def save_users(users):
    path = get_data_path("user_data.json")

    with open(path, "w") as file:
        json.dump(users, file, indent=4)
    '''Saves users data'''


def create_user(password, name, email, role="user"):
    users = load_user_data()

    user_id = generate_user_id(users)

    users[user_id] = {
        "password": password,
        "name": name,
        "role": role,
        "balance": 0,
        "email": email
    }

    save_users(users)

    return user_id
    '''Makes new user'''

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
   


def generate_user_id(users):
    while True:
        new_id = str(random.randint(100, 999))

        if new_id not in users:
            return new_id







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