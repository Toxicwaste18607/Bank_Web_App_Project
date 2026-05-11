
import streamlit as st
from non_page_code.auth import *
from app_pages.Transactions import *
from app_pages.Dashboard import *
from classes.user import User
from classes.admin import Admin
from app_pages.Transaction_History import show_transactions




def admin_users_page():
    users = load_user_data()

    st.header("Admin - User Accounts")

    for user_id, user_data in users.items():
        st.write(f"ID: {user_id}")
        st.write(f"Name: {user_data['name']}")
        st.write(f"Username: {user_data['username']}")
        st.write(f"Role: {user_data['role']}")
        st.write(f"Balance: ${user_data['balance']:,.2f}")
        st.write(f"Locked: {user_data.get('locked', False)}")

        '''if user_data.get("locked", False):
            if st.button(f"Unlock {user_id}"):
                set_account_lock(user_id, False)
                st.rerun()
        else:
            if st.button(f"Lock {user_id}"):
                set_account_lock(user_id, True)
                st.rerun()'''

        st.divider()