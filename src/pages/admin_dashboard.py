import streamlit as st

st.write("Not Implemented Yet")

import streamlit as st

def show_admin_page(user):
    st.title("Admin Page")

    if not user.is_admin():
        st.error("Access denied.")
        return

    st.write("Admin controls go here.")