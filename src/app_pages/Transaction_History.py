import streamlit as st
from .Transactions import *
from classes.user import User
from classes.admin import Admin
from non_page_code.storage import load_transactions





def show_transactions():
    left, mid, right = st.columns([.5, 4, .5])

    transactions = load_transactions()

    user = st.session_state.user

    recent_transactions = transactions.get(user.user_id, [])

    if user.role == "user":

        with mid:
            st.title("Transaction History")
            st.write(f"Welcome, {user.name}")


            if len(recent_transactions) == 0:
                st.write("No transactions found.")

            else:
                for transaction in recent_transactions:
                    st.write(transaction["date"])
                    st.write(transaction["type"])
                    st.write(transaction["amount"])