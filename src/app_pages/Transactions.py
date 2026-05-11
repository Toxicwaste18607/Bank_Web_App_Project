import streamlit as st
from non_page_code.storage import save_users, load_user_data




def withdrawal_page():
    user = st.session_state.user

    with st.form("withdrawal_form"):
        
        money_out=st.number_input("What is the amount you would like to withdraw.")
        summitted= st.form_submit_button("Confirm transaction")

        if summitted:
            result = user.withdrawal(money_out)


            if result == True:
                st.write(f"${money_out} has been withdrawn from your account.")
            if result == None:
                st.write("Your balance is too low")
            if result == False:
                st.write("You cannot Withdraw less then $0.01")



def deposit_page():
    user = st.session_state.user

    with st.form("deposit_form"):
        money_in=st.number_input("How much money would you like to deposit.")
        summitted= st.form_submit_button("Confirm transaction")

        if summitted:
            result=user.deposit(money_in)
            if result is None:
                st.write("You cannot deposit less then $0.01.")
            if result is not None:
                st.write(f"${money_in} has been added to your account.")



     



