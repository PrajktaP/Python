class BankAccount:
    def __init__(self, acc_num, name, balance):
        self.acc_num = acc_num
        self.name = name
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount

    def withdraw(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount

    def display(self):
        print("Balance: ", self.balance)

def main():
    try: 
        obj1 = BankAccount('100', 'Prajkta', 5000)
        obj1.display()

        deposit_amount = float(input("Enter the amount you want to deposit: "))
        obj1.deposit(deposit_amount)
        obj1.display()

        withdraw_amount = float(input("Enter the amount you want to withdraw: "))
        obj1.withdraw(withdraw_amount)
        obj1.display()
    except ValueError as vobj:
        print("Invalid value entered: ", vobj)
    except Exception as eobj:
        print("Exception occurred: ", eobj)

if __name__ == "__main__":
    main()


"""
5. Create a class BankAccount with account_number, name, and balance. Use
__init__ and create methods for deposit, withdraw, and displaying balance.
"""