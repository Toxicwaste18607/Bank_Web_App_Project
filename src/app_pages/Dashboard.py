import streamlit as st
from .Transactions import *



def show_dashboard_page():
    left,mid,right=st.columns([1,2,1])


    user = st.session_state.user
    st.session_state.current_page ='home'
    
   

    with mid:
        st.title("Dashboard")
        st.write(f"Welcome, {user.name}")

        st.write(f"Current Balance is ${user.balance:,.2f}")








