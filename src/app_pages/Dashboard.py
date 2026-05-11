import streamlit as st
from .Transactions import *
from classes.user import User
from classes.admin import Admin
from non_page_code.storage import load_transactions


def show_dashboard_page():
    left,mid,right=st.columns([1,4,1])
    transaction = load_transactions()

    user = st.session_state.user


    
<<<<<<< HEAD
def show_dashboard_page():
    left, mid, right = st.columns([1, 4, 1])
    transactions = load_transactions()

    user = st.session_state.user

    if user.role == "user":
        user_transactions = transactions.get(user.user_id, [])
=======
    if user.role=='user':
        recent_transactions=transaction[user.user_id][-3:]
>>>>>>> c2c7408106d9fdce64f8ec3e712cd22779f6c64a

        with mid:
            st.title("Dashboard")
            st.write(f"Welcome, {user.name}")
<<<<<<< HEAD
            st.write(f"Current Balance is ${user.balance:,.2f}")

            recent_transactions = user_transactions[-3:]

            if len(recent_transactions) == 0:
                st.write("No transactions yet.")
            else:
                for transaction in recent_transactions:
                    st.write(transaction["date"])
                    st.write(transaction["type"])
                    st.write(transaction["amount"])
=======

            st.write(f"Current Balance is ${user.balance:,.2f}")
            for transaction in recent_transactions:
                st.write(transaction["date"])
                st.write(transaction["type"])
                st.write(transaction["amount"])
>>>>>>> c2c7408106d9fdce64f8ec3e712cd22779f6c64a



    
    if user.role=='admin':
        with mid:
            st.write('Admin dashboard')









