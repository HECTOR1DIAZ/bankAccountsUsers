class BankAccount:		# declare a class and give it name User
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        # self.name = "BA1"

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if amount > self.balance:
            print ("INVALID TRANSACTION")
        else:
            self.balance-= amount
            print (self.balance)
        return self

    def display_account_info(self):
        print('Balance: ' + '$' + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        else:
            print ("INVALID TRANSACTION")
        return self

class User:		# declare a class and give it name User
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0.00
    
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance + amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount	
        return self

    def display_user_balance(self):
        print('User: ' + self.name + ',Balance: $' + str(self.account_balance))
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


jordan = User("Jay Wade", "email@email.com")
matthew = User("Matthew Wade", "mat@email.com")
oliver = User("Oliver Wade", "oli@email.com")


jordan.make_deposit(200).make_deposit(200).make_deposit(50).make_withdrawal(5).display_user_balance()
oliver.make_deposit(40000).make_deposit(200).make_withdrawal(200).make_withdrawal(50).make_withdrawal(5).make_withdrawal(200).display_user_balance()





