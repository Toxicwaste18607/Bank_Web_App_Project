import streamlit as st




def show_dashboard_page():
    user = st.session_state.user

    st.title("Dashboard")
    st.write(f"Welcome, {user.name}")

    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()


