def accept():
    try:
        value1 = int(input("Enter first number: "))
        value2 = int(input("Enter second number: "))
        return value1, value2
    except ValueError as vobj:
        print("Invalid input! Please enter numeric values.", vobj)

class Calculator:
    def __init__(self, value1, value2):
        print("Inside constructor")
        self.value1 = value1
        self.value2 = value2

    def addition(self, value1, value2):
        ans = value1 + value2
        return ans

    def subtraction(self, value1, value2):
        ans = value1 - value2
        return ans

    def multiplication(self, value1, value2):
        ans = value1 * value2
        return ans

    def division(self, value1, value2):
        ans = value1 / value2
        return ans

    def __del__(self):
        print("Inside destructor")

def main():
    value1, value2 = accept()

    obj = Calculator(value1, value2)

    add = obj.addition(value1, value2)
    print("Addition result is: ", add)

    sub = obj.subtraction(value1, value2)
    print("Subtraction result is: ", sub)

    multi = obj.multiplication(value1, value2)
    print("Multiplication result is: ", multi)

    div = obj.division(value1, value2)
    print("Division result is: ", div)

if __name__ == "__main__":
    main()



"""
6. Create a class Calculator with methods for add, subtract, multiply, divide. Ask user
input for values and call methods accordingly.
"""