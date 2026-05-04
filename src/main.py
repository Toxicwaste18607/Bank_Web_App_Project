import streamlit as st

#from models import User
from pages.dashboard import show_dashboard_page
from pages.transactions import show_transactions_page
from pages.admin_dashboard import show_admin_page


def login_page():
    st.title("Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        role = st.selectbox("Role", ["user", "admin"])
        submitted = st.form_submit_button("Login")

        if submitted:
            st.session_state.user = User(username, role)
            st.rerun()


if "user" not in st.session_state:
    st.session_state.user = None


if st.session_state.user is None:
    login_page()

else:
    user = st.session_state.user

    pages = ["Dashboard", "Transactions"]

    if user.is_admin():
        pages.append("Admin")

    selected_page = st.sidebar.radio("Pages", pages)

    if selected_page == "Dashboard":
        show_dashboard_page(user)

    elif selected_page == "Transactions":
        show_transactions_page(user)

    elif selected_page == "Admin":
        show_admin_page(user)

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()