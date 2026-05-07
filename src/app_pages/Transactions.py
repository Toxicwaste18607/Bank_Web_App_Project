import streamlit as st



def withdrawal():
    col1, col2 = st.columns(2)

    with col1:
        st.write("Left")

    with col2:
        st.write("Right")

def deposit():pass


def show_transactions_page():

    choice = st.radio ("Choose", ["Withdrawal","Deposit"])
    if choice == "Withdrawal":
        withdrawal()
    if choice== "Deposit":
        deposit()







