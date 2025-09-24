def main():
    num1 = input("Enter a number: ")

    Addition = 0
    
    for digit in num1:
        Addition = Addition + int(digit)

    print(f"Addition of the digits in {num1} are: ", Addition)

if __name__ == "__main__":
    main()


"""
10. Write a program which accept number from user and return addition of digits in that number.
Input: 5187934
Output : 37
"""