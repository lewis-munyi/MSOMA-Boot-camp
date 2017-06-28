class Account:
    rate = 5
    def __init__(self, account_holder):
        self.holder = account_holder                                                                      
        self.balance = 0                                                                                                                                                                        
    def deposit(self, amount):
        self.balance += int(amount)
        return self.balance

    def withdraw(self, amount):
        assert self.balance > amount, "You cannot withdraw more than you have in your account" 
        self.balance = self.balance - amount
        return self.balance
    def interest(self):
        total = self.balance * Account.rate / 100 * 2 
        self.balance += total 
        return print ('Hi ' + str(self.holder) + ' your total interest is ' + str(total) + ' and your total balance is ' + str(self.balance))
