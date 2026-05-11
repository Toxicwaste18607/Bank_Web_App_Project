from non_page_code.storage import save_balance, add_transaction





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
            save_balance(self)
        return True






    def deposit(self,money_in):
        

        self.balance += money_in

        save_balance(self)
        add_transaction(self,'deposit',money_in)
        return 

