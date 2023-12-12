class BankAccount:
	def __init__(self, account_number, account_holder_name,account_type, balance=0.0):
		self.account_number = account_number
		self.account_holder_name = account_holder_name
		self.account_type = account_type
		self.balance = balance
	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			print("deposit of ",amount," successful.New balance:" ,self.balance)
		else:
			print("invalid deposite amount.please enter a positive value.")
	def withdraw(self,amount):
		if 0 < amount<=self.balance:
			self.balance-=amount
			print("withdrawal of ",amount," successful.new balance:",self.balance)
		else:
			print("invalid withdrawalamout or insufisent funds.")
	def display_account_info(self):
		print("Account Number: ",self.account_number)
		print("Account Holder: ",self.account_holder_name)
		print("Account Type: ",self.account_type)
		print("Current Balance:",self.balance)
account1 = BankAccount("123456","john doe","saving",1000.0)
account1.display_account_info()
account1.deposit(500.0)
account1.withdraw(200.0)
account1.display_account_info()

