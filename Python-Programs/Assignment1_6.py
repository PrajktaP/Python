def main():
    value = int(input("Enter number: "))

    if value < 0:
        print("Negative number")
    elif value > 0:
        print("Positive number")
    else:
        print("Zero")

if __name__ == "__main__":
    main()


"""
6. Write a program which accept number from user and check whether that number is positive or negative or zero.
Input : 11                  Output: Positive number 
Input : -8                  Output: Negative number
Input : 0                   Output: Zero
"""