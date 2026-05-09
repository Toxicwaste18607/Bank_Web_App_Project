class User:
    def __init__(self, user_id, name, username,role, balance, email):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.balance = balance
        self.email = email
        self.user_name=username


    def status(self):
        return self.role