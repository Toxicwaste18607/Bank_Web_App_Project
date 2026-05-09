import streamlit as st
from .Transactions import *



def show_dashboard_page():
    left,mid,right=st.columns(3)


    user = st.session_state.user
    st.session_state.current_page ='home'
    st.title("Dashboard")
   

    with mid:
        st.write(f"Welcome, {user.name}")

        st.write(f"Current Balance is ${user.balance:,.2f}")








