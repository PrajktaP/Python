import Arithmatic as Ar

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    add = Ar.Add(num1, num2)
    print("Addition result is: ", add)

    sub = Ar.Sub(num1, num2)
    print("Subtraction result is: ", sub)

    multi = Ar.Multi(num1, num2)
    print("Multiplication result is: ", multi)

    div = Ar.Div(num1, num2)
    print("Division result is: ", div)

if __name__ == "__main__":
    main()


"""
Q1. Arithmetic Operations on Two Numbers.
Write a program to accept two integers from the user and display their:
• Sum
• Difference
• Product
• Division

Expected Input:
Enter first number: 10
Enter second number: 2

Expected Output:
Sum: 12
Difference: 8
Product: 20
Division: 5.0
"""