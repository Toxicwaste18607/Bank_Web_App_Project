import streamlit as st




def withdrawal():
    st.write("withdrawal")

def deposit():
    st.write("deposit")



def withdrawal_page():
    with st.form(withdrawal_form):


def deposit_page():




def show_transactions_page():
    columns = st.columns(2)

    col1=columns[0]
    col2=columns[1]
    
    with col1:
        if st.button("Withdrawal"):
            withdrawal()


    with col2:
        if st.button("Deposit"):
            deposit()






