import streamlit as st


if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please log in first.")
    st.stop()


def show_dashboard_page():
    user = st.session_state.user

    st.title("Dashboard")
    st.write(f"Welcome, {user.username}")


show_dashboard_page()