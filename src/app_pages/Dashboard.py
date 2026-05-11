import streamlit as st
from .Transactions import *
from classes.user import User
from classes.admin import Admin
from non_page_code.storage import load_transactions


def show_dashboard_page():
    left,mid,right=st.columns([1,2,1])
    transactions = load_transactions()

    user = st.session_state.user
    recent_transactions=transactions[user.user_id][-3:]

    
    
    if user.role=='user':

        with mid:
            st.title("Dashboard")
            st.write(f"Welcome, {user.name}")

            st.write(f"Current Balance is ${user.balance:,.2f}")



    
    if user.role=='admin':
        with mid:
            st.write('Admin dashboard')









