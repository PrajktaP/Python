multiplication = lambda num1, num2 : num1 * num2

def main():
    try:
        input_number1 = int(input("Enter first number: "))
        input_number2 = int(input("Enter second number: "))

        resp = multiplication(input_number1, input_number2)

        print(f"multiplication of {input_number1} and {input_number2} is: {resp}")
    except ValueError as vobj:
        print("Incorrect value entered: ", vobj)
    except Exception as eobj:
        print("An exception occurred: ", eobj)

if __name__ == "__main__":
    main()

"""
2.Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
Input : 4 3 Output : 12
Input : 6 3 Output : 18
"""