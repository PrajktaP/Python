Multiply = lambda x, y : x * y

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Find Power of the number
    Ans = Multiply(num1, num2)
    print(f"Result of the multiplication of {num1} and {num2} is: ", Ans)

if __name__ == "__main__":
    main()

"""
2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.
Input : 4 3    Output : 12
Input : 6 3    Output : 18
"""