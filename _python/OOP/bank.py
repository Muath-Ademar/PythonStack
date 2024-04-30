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

