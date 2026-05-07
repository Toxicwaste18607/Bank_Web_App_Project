import streamlit as st




def withdrawal():pass

def deposit():pass


def show_transactions_page():
    columns = st.columns(2)

    col1=columns[0]
    col2=columns[1]
    
    with col1:
        st.button("Withdrawal")
        

    with col2:
        st.button("Deposit")






