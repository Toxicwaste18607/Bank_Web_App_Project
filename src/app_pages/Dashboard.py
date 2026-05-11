import streamlit as st
from non_page_code.storage import load_transactions


def show_dashboard_page():
    left, mid, right = st.columns([1, 4, 1])
    transactions = load_transactions()

    user = st.session_state.user

    if user.role == "user":
        recent_transactions = transactions.get(user.user_id, [])[-3:]

        with mid:
            st.title("Dashboard")
            st.write(f"Welcome, {user.name}")
            st.write(f"Current Balance is ${user.balance:,.2f}")

            if len(recent_transactions) == 0:
                st.write("No transactions yet.")
            else:
                for transaction in recent_transactions:
                    st.write(transaction["date"])
                    st.write(transaction["type"])
                    st.write(transaction["amount"])

    if user.role == "admin":
        with mid:
            st.write("Admin dashboard")