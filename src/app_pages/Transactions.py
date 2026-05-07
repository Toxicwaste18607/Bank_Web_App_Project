import streamlit as st




def withdrawal():
    st.write("withdrawal")

def deposit():
    st.write("deposit")



def withdra



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






