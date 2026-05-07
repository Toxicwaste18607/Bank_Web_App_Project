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
    path = get_data_path("user_data.json")

    with open(path, "w") as file:
        json.dump(users, file, indent=4)






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
    with st.form("login_form"):
        user_id = st.text_input("Enter your user ID")

        password = st.text_input(
            "Enter your password",
            type="password"
        )

        submitted = st.form_submit_button("Login")

        if submitted:
            user = check_login(user_id, password)

            if user is not None:
                st.session_state.user = user
                st.success("Logged in!")
                st.rerun()

            else:
                st.error("Invalid login")

def create_new_account(): 
    st.header("New User")

    with st.form("new_user_form"):
        name = st.text_input("Enter your name")
        password = st.text_input("Enter a password", type="password")
        email = st.text_input("Email")

        submitted = st.form_submit_button("Create Account")

        if submitted:
            new_id = create_user(password, name, email)
            st.success(f"Account created! Your user ID is {new_id}")


        

    


def hello_page(): 
    user = st.session_state.user
    st.write (f'Welcome {user.username} ')





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