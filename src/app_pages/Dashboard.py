import streamlit as st
from .Transactions import *



def show_dashboard_page():
    
    user = st.session_state.user
    st.session_state.current_page ='home'
    st.title("Dashboard")
    st.write(f"Welcome, {user.name}")

    st.write(f"Current Balance is ${user.balance:,.2f}")







