import streamlit as st
import random
import os
import json

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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


def create_user(password, name,username, email, role="user"):
    users = load_user_data()

    user_id = generate_user_id(users)

    users[user_id] = {
        "password": password,
        "name": name,
        "username":username,
        "role": role,
        "balance": 0,
        "email": email
    }

    save_users(users)

    return user_id
    '''Makes new user'''


def generate_user_id(users):
    while True:
        new_id = str(random.randint(100, 999))

        if new_id not in users:
            return new_id
        
def save_balance(user):
    users = load_user_data()

    users[user.user_id]["balance"] = user.balance

    save_users(users)

