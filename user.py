class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount
    def make_withdrawal(self,amount):
        if amount < self.account_balance:
            self.account_balance -= amount
        else:
            print (f"The amount requested is higher than the account balance (${self.account_balance})")
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


#Create 3 instances of the User class

Juan = User("Juan", "juan@gmail.com")
Ana = User("Ana","ana@yahoo.com")
Pedro = User("Pedro", "pedro@hola.com")

#Have the first user make 3 deposits and 1 withdrawal and then display their balance

Juan.make_deposit(100)
Juan.make_deposit(50)
Juan.make_deposit(200)
Juan.make_withdrawal(25)
Juan.display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance

Ana.make_deposit(1000)
Ana.make_deposit(40)
Ana.make_withdrawal(10)
Ana.make_withdrawal(15)
Ana.display_user_balance()

#Have the third user make 1 deposits and 3 withdrawals and then display their balance

Pedro.make_deposit(150)
Pedro.make_withdrawal(50)
Pedro.make_withdrawal(75)
Pedro.make_withdrawal(50)
Pedro.display_user_balance()

#BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

Juan.transfer_money(Pedro,200)
Juan.display_user_balance()
Pedro.display_user_balance()
