from non_page_code.storage import save_users



class User:
    def __init__(self, user_id, name, username,role, balance, email):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.balance = balance
        self.email = email
        self.username=username


    def withdrawal(self,money_out):

        temp_balance = self.balance

        temp_balance-=money_out


        if temp_balance < 0:
            return None
        else:
            self.balance -= money_out
            save_users(self.balance)
        return 






    def deposit(self,money_in):
        

        self.balance += money_in

        save_users(self.balance)
        return 

