import streamlit as st
from non_page_code.storage import save_users, load_user_data



def withdrawal(money_out):
    user = st.session_state.user
    users = load_user_data()


    temp_balance = user.balance

    temp_balance-=money_out


    if temp_balance <0:
        return None
    else:
        user.balance -= money_out
        users[user.user_id]["balance"]=user.balance
        save_users(users)
    return user






def deposit(money_in):
    user = st.session_state.user
    users = load_user_data()


    user.balance += money_in

    users[user.user_id]["balance"] = user.balance
    save_users(users)
    return user


def withdrawal_page():
    with st.form("withdrawal_form"):
        
        money_out=st.number_input("What is the amount you would like to withdraw.")
        summitted= st.form_submit_button("Confirm transaction")

        if summitted:
            result = withdrawal(money_out)


            if result is not None:
                st.write("Transaction complete")
            else:
                st.write("Your balance is to low")



def deposit_page():
    with st.form("deposit_form"):
        money_in=st.number_input("How much money would you like to deposit.")
        summitted= st.form_submit_button("Confirm transaction")

        if summitted:
            deposit(money_in)
            st.write(f"{money_in} has been added to your account.")



def show_transactions_page():

    if "transaction_type" not in st.session_state:
        st.session_state.transaction_type = None
    columns = st.columns(2)

    col1=columns[0]
    col2=columns[1]
    
    with col1:
        if st.button("Withdrawal"):
            st.session_state.transaction_type = "withdrawal"

    with col2:
        if st.button("Deposit"):
            st.session_state.transaction_type = "deposit"

    if st.session_state.transaction_type == "withdrawal":
        withdrawal_page()

    elif st.session_state.transaction_type == "deposit":
        deposit_page()
     



