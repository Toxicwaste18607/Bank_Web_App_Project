import streamlit as st
from non_page_code.storage import save_users



def withdrawal(money_out):
    user = st.session_state.user

    if user.balance <=0:
        return None
    else:
        user.balance -= money_out
        save_users()






def deposit(money_in):
    user = st.session_state.user

    user.balance += money_in
    save_users()



def withdrawal_page():
    with st.form("withdrawal_form"):
        
        money_out=st.text_input("What is the amount you would like to withdraw.")
        summitted= st.form_submit_button("Confirm transaction")

        if summitted:
            withdrawal(money_out)

            if withdrawal is not None:
                st.write("Transaction complete")
            else:
                st.write("Your balance is to low")



def deposit_page():
    with st.form("depoit_form"):
        money_in=st.text_input("How much money would you like to deposit.")
        summitted= st.form_submit_button("Confirm transaction")

        if summitted:
            deposit(money_in)



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






