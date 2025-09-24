import Arithmatic as Ar

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    addAns = Ar.Add(num1, num2)
    print("Result of Add is: ", addAns)

    subAns = Ar.Sub(num1, num2)
    print("Result of Sub is: ", subAns)

    multiAns = Ar.Multi(num1, num2)
    print("Result of Multi is: ", multiAns)

    divAns = Ar.Div(num1, num2)
    print("Result of Div is: ", divAns)

if __name__ == "__main__":
    main()


"""
1. Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult) for multiplication and Div()
for division.
All functions accepts two parameters as number and perform the operation. 
Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.
"""