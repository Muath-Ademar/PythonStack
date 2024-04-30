class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance = 0
    def makedeposit(self, amount):
        self.balance= self.balance+amount
        return self
    def makeWhithdrawal(self, amount):
        self.balance= self.balance-amount
        return self
    def displayUserbalance(self):
        print(self.balance)
        return self

mike = User("mike", "mike@gmail.com")
muath = User("muath", "muath@gmail.com")
Tony = User("Tony", "Tony@gmail.com")

mike.makedeposit(200).makedeposit(200).makedeposit(200).makeWhithdrawal(100).displayUserbalance()
muath.makedeposit(200).makedeposit(200).makeWhithdrawal(100).makeWhithdrawal(50).displayUserbalance()
Tony.makedeposit(1000).makeWhithdrawal(200).makeWhithdrawal(200).makeWhithdrawal(200).displayUserbalance()