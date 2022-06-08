

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def printRunningTotal(self):
        print(f"{self.name} has {self.account_balance} dollars in the bank")
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(f"{self.name} took out {amount} from their bank acount")
        self.printRunningTotal()
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"{self.name} deposited {amount} into thier bank acount")
        self.printRunningTotal()
        return self

    def transfer_money(self, User, amount):
        print(f"We are making a transfer from {self.name} to {User.name} with this amount {amount}")
        self.make_withdrawal(amount)
        User.make_deposit(amount)
        return self


guido = User("Guido van Rossum", "guido@python.com") # created a User named Guido
monty = User("Monty Python", "monty@python.com") # created a User named Montry
elmo = User("Elmo", "elmo@sesemestreet.com")

print(guido.name) 
print(monty.name)

print('*'*25)
guido.make_deposit(1000)
print('*'*25)
monty.make_deposit(10)
print('*'*25)
print('*'*25)

print(guido.account_balance)
print('*'*25)
print(monty.account_balance)
print('*'*25)
print('*'*25)
guido.transfer_money(monty, 50)
print('*'*25)
print(guido.account_balance)
print('*'*25)
print(monty.account_balance)
print('*'*25)


guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).printRunningTotal()

