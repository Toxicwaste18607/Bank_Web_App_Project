import os
import streamlit as st 
import json
import random



APP_PATH = os.path.dirname(os.path.abspath(__file__))


def get_data_path(filename: str) -> str:
    '''Returns the path to an asset file, given its filename.'''
    return os.path.join(APP_PATH, "data", filename)



def load_user_data():
    path= get_data_path("user_data.json")

    if not os.path.exists(path):
        return {}
    
    with open (path,'r') as file:
        return json.load(file)
    



def save_users(users):
    path = get_data_path("users_data.json")

    with open(path, "w") as file:
        json.dump(users, file, indent=4)






def create_user(user_id, password, name, email, role="user"):
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
    return True


def check_login(user_id, password):
    users = load_user_data()

    if user_id in users:
        if users[user_id]["password"] == password:
            user_data = users[user_id]

            return User(
                username=user_id,
                role=user_data["role"]
            )

    return None


def generate_user_id(users):
    while True:
        new_id = str(random.randint(100, 999))

        if new_id not in users:
            return new_id




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


            st.session_state.user = User(username,role)
            st.success ("Logged in")
            st.rerun()

def create_new_account(): 
    st.header("New User")

    with st.form("new_user_form"):
        name=st.text_input("Enter your name")
        password= st.text_input("Enter a password" , type="password")
        email= st.text_input("Email")

        

    


def hello_page(): 
    user = st.session_state.user
    st.write (f'Welcome {user.username} ')





#app code here


if "user" not in st.session_state:
    st.session_state.user=None
    login_page()

else:
    hello_page()