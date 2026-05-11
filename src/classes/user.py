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
        if money_out <=0:   
            return False

        else:



            temp_balance = self.balance


            temp_balance-=money_out
            if temp_balance < 0:
                return None
            else:
                self.balance -= money_out
                save_balance(self)
                add_transaction(self,'withdrawal',money_out)
        return True






    def deposit(self,money_in):
        
        if money_in <=0:
            return None
        else:
            self.balance += money_in
            self.balance=round(self.balance,2)
            save_balance(self)
            add_transaction(self,'deposit',money_in)

        
<<<<<<< HEAD
        return True
=======
        return 
>>>>>>> c2c7408106d9fdce64f8ec3e712cd22779f6c64a

