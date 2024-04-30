class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance = 0
    def makedeposit(self, amount):
        self.balance= self.balance+amount
    def makeWhithdrawal(self, amount):
        self.balance= self.balance-amount
    def displayUserbalance(self, amount):
        print(self.balance)

mike = User("mike", "mike@gmail.com")
muath = User("muath", "muath@gmail.com")
Tony = User("Tony", "Tony@gmail.com")

mike.makedeposit(200)
mike.makedeposit(200)
mike.makedeposit(200)
mike.makeWhithdrawal(100)
mike.displayUserbalance("amount")

muath.makedeposit(200)
muath.makedeposit(200)
muath.makeWhithdrawal(100)
muath.makeWhithdrawal(50)
muath.displayUserbalance("amount")

Tony.makedeposit(1000)
Tony.makeWhithdrawal(200)
Tony.makeWhithdrawal(200)
Tony.makeWhithdrawal(200)
Tony.displayUserbalance("amount")