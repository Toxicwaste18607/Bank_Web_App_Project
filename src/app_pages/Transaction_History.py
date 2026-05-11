import streamlit as st
from .Transactions import *
from classes.user import User
from classes.admin import Admin
from non_page_code.storage import load_transactions





def show_transactions():
<<<<<<< HEAD
    left, mid, right = st.columns([.5, 4, .5])

    transactions = load_transactions()

    user = st.session_state.user

    recent_transactions = transactions.get(user.user_id, [])

    if user.role == "user":
=======
    left,mid,right=st.columns([.5,4,.5])
    transaction = load_transactions()

    user = st.session_state.user
    recent_transactions=transaction[user.user_id]


    
    if user.role=='user':
>>>>>>> c2c7408106d9fdce64f8ec3e712cd22779f6c64a

        with mid:
            st.title("Transaction History")
            st.write(f"Welcome, {user.name}")

<<<<<<< HEAD

            if len(recent_transactions) == 0:
                st.write("No transactions found.")

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
