
def CheckOddEven(Num):
    if Num % 2 == 0:
        print(f"{Num} is an even number.")
    else:
        print(f"{Num} is an odd number.")

def main():
    Num = input("Enter a Number: ")

    while not Num.isnumeric():
        Num = input("Invalid input. Enter a Number: ")

    CheckOddEven(int(Num))

if __name__ == "__main__":
    main()


"""
Q5. Even or Odd Number Check
Write a program to check whether the entered number is even or odd.
Expected Input:
Enter a number: 17
Expected Output:
17 is an odd number.
"""