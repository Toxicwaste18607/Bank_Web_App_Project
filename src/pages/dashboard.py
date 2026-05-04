import streamlit as st

def show_dashboard_page(user):
    st.title("Dashboard")
    st.write(f"Welcome, {user.username}")