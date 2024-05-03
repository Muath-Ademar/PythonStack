class BankAccount:
	def __init__(self, int_rate, balance):
		self.interest = int_rate
		self.balance = balance
	def deposit(self, amount):
		self.balance = self.balance + amount
		return self
	def withdraw(self, amount):
		if amount>self.balance:
			self.balance= self.balance-5
			print("Insufficient funds: Charging a $5 fee" ) 
			return self
		else:
			self.balance= self.balance - amount
		return self
	def display_account_info(self):
		print(self.balance)
		return self
	def yield_interest(self):
		if self.balance>0:
			self.balance +=  self.balance * self.interest
		return self

accountA=BankAccount(0.03, 100)
accountB=BankAccount(0.01, 100)

accountA.deposit(100).deposit(150).deposit(350).withdraw(100).yield_interest().display_account_info()	
accountB.deposit(300).deposit(450).withdraw(200).withdraw(200).withdraw(200).withdraw(300).yield_interest().display_account_info()

class User:
    def __init__(self, name, email_address, int_rate=0.02, balance=0):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate , balance )
    def makedeposit(self, amount):
        self.account.deposit(amount)
        return self
    def makeWhithdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def displayUserbalance(self):
        print(self.account.balance)
        return self

mike = User("mike", "mike@gmail.com",0.03, 300)
muath = User("muath", "muath@gmail.com",0.04, 400)
Tony = User("Tony", "Tony@gmail.com", 0.05, 250)

print(mike.account.balance)
mike.makedeposit(200).makedeposit(200).makedeposit(200).makeWhithdrawal(100).displayUserbalance()
muath.makedeposit(200).makedeposit(200).makeWhithdrawal(100).makeWhithdrawal(50).displayUserbalance()
Tony.makedeposit(1000).makeWhithdrawal(200).makeWhithdrawal(200).makeWhithdrawal(200).displayUserbalance()