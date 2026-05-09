import streamlit as st
from .classes import *
from .storage import *



def check_login(user_id,username, password):
    users = load_user_data()

    for user_id, user_data in users.items():
        user_data = users[user_id] 

        if user_id in users or user_data["username"] == username:
            if user_data["password"] == password:
                return User(
                    user_id=user_id,
                    name=user_data["name"],
                    user_name=user_data["user_name"],
                    role=user_data["role"],
                    balance=user_data["balance"],
                    email=user_data["email"]
                )
        
        
        

    return None