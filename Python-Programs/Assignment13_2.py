class BankAccount:
    rate_of_interest = 10.5

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self, deposit_amount):
        self.amount = self.amount + deposit_amount

    def withdraw(self, withdraw_amount):
        self.amount = self.amount - withdraw_amount

    def calculate_interest(self):
        interest = (self.amount * BankAccount.rate_of_interest) / 100
        return interest

    def display(self):
        print("Name: ", self.name)
        print("Amount: ", self.amount)

def main():
    try: 
        obj1 = BankAccount('Prajkta', 5000)

        deposit_amount = float(input("Enter the amount you want to deposit: "))
        obj1.deposit(deposit_amount)

        withdraw_amount = float(input("Enter the amount you want to withdraw: "))
        obj1.withdraw(withdraw_amount)

        interest = obj1.calculate_interest()
        print("Interest: ", interest)

        obj1.display()
    except ValueError as vobj:
        print("Invalid value entered: ", vobj)
    except Exception as eobj:
        print("Exception occurred: ", eobj)

if __name__ == "__main__":
    main()



"""
2. Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialise to 10.5.
Inside init method initialise all name and amount variables by accepting the values from user.
There are
Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable
Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects.
"""