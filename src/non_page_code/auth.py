import streamlit as st
from classes.user import User
from .storage import *



def check_login(user_info, password):
    users = load_user_data()

    for user_id, user_data in users.items():
        user_data = users[user_id] 

        if user_info in users or user_data["username"] == user_info:
            if user_data["password"] == password:
                return User(
                    user_id=user_id,
                    name=user_data["name"],
                    username=user_data["username"],
                    role=user_data["role"],
                    balance=user_data["balance"],
                    email=user_data["email"]
                )
        
        
        

    return None