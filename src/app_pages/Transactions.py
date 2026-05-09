import streamlit as st
from non_page_code.storage import save_users, load_user_data
from classes.user import User
from classes.admin import Admin



def withdrawal_page():
    with st.form("withdrawal_form"):
        
        money_out=st.number_input("What is the amount you would like to withdraw.")
        summitted= st.form_submit_button("Confirm transaction")

        if summitted:
            result = user.withdrawal(money_out)


            if result is not None:
                st.write(f"${money_out} has been withdrawn from your account.")
            else:
                st.write("Your balance is too low")



def deposit_page():
    with st.form("deposit_form"):
        money_in=st.number_input("How much money would you like to deposit.")
        summitted= st.form_submit_button("Confirm transaction")

        if summitted:
            deposit(money_in)
            st.write(f"${money_in} has been added to your account.")



     



