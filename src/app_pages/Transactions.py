import streamlit as st




def withdrawal():
    st.write("withdrawal")

def deposit():
    st.write("deposit")



def withdrawal_page():
    with st.form("withdrawal_form"):
        
        money_out=st.text_input("What is the amount you would like to withdraw.")
        summitted= st.form_submit_button("Confirm transaction")

        if summitted:
            withdrawal()



def deposit_page():
    with st.form("depoit_form"):
        money_in=st.text_input("How much money would you like to deposit.")
        summitted= st.form_submit_button("Confirm transaction")

        if summitted:
            deposit()



def show_transactions_page():
    columns = st.columns(2)

    col1=columns[0]
    col2=columns[1]
    
    with col1:
        if st.button("Withdrawal"):
            withdrawal_page()


    with col2:
        if st.button("Deposit"):
            deposit_page()






