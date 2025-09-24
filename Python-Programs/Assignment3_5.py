from MarvellousNum import ChkPrime
from functools import reduce

Sum = lambda num1, num2 : num1 + num2
ListPrime = lambda PrimeData : print("Prime numbers: ", PrimeData)

def main():
    # get number of elements
    size = int(input("Enter number of elements: "))
    
    # get the size of elements from users
    Data = []
    for no in range(size):
        Data.append(int(input("Enter number: ")))
    print("Input elements: ", Data)

    # find prime numbers from the numbers entered by user
    PrimeData = list(filter(ChkPrime, Data))

    ListPrime(PrimeData)

    # Addition of prime numbers
    Addition = reduce(Sum, PrimeData)
    print("Addition of all prime numbers: ", Addition)

if __name__ == "__main__":
    main()


"""
5. Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List.
Main python file accepts N numbers from user and 
pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. 
Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output: 54(13+5+7+2+5)
"""