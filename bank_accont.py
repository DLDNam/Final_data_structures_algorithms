import os

def menu():
    print("1: deposit")
    print("2: withdraw")
    print("3: get balance")
    print("4: get transaction history")
    print("5: exit")
class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(("deposit", amount, self.balance))

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(("withdraw", amount, self.balance))
        else:
            print("Transaction failed")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history

# Tạo một tài khoản mới với số tài khoản là "123456", chủ tài khoản là "John Doe" và số dư khởi đầu là 1000 đô la.
account = BankAccount(str(input("account_number: ")), str(input("Owner: ")), int(input("Balance: ")))
choice = 0
while (choice != 5):    
    os.system('cls')
    menu()
    choice = int(input("Input your choice: "))
    if choice == 1: 
        account.deposit(int(input("Enter the amount to be added to the Account: ")))
        input("Enter ")
    elif choice ==2:
        account.withdraw(int(input("Withdraw: ")))
        input("Enter ")
    elif choice == 3:
        print( 'The remaining balance in the account is: ',account.get_balance())
        input("Enter ")
    elif choice == 4:
        print(account.get_transaction_history())
        input("Enter ")        
    elif choice == 5:
        break
