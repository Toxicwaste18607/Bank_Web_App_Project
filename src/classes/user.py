class User:
    def __init__(self, user_id, name, username,role, balance, email):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.balance = balance
        self.email = email
        self.username=username


        def withdrawal(money_out):
            user = st.session_state.user
            users = load_user_data()


            temp_balance = user.balance

            temp_balance-=money_out


            if temp_balance < 0:
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

