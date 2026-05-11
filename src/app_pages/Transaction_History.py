import streamlit as st
from .Transactions import *
from classes.user import User
from classes.admin import Admin
from non_page_code.storage import load_transactions





def show_transactions():
    left,mid,right=st.columns([1,4,1])
    transaction = load_transactions()

    user = st.session_state.user
    recent_transactions=transaction[user.user_id]


    
    if user.role=='user':

        with mid:
            st.title("Transaction History")
            st.write(f"Welcome, {user.name}")

            st.write(f"Current Balance is ${user.balance:,.2f}")
            for transaction in recent_transactions:
                st.write(transaction["date"])
                st.write(transaction["type"])
                st.write(transaction["amount"])