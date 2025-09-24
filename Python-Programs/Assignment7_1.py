
Square = lambda num : num ** 2
Cube = lambda num : num ** 3

def main():
    num = int(input("Enter a number: "))

    SqAns = Square(num)
    print(f"Square of {num} is: ", SqAns)

    CuAns = Cube(num)
    print(f"Cube of {num} is: ", CuAns)

if __name__ == "__main__":
    main()

"""
Q1. Write two lambda functions:
• One to calculate square of a number
• Another to calculate cube of a number
Expected Input:
Enter a number: 3
Expected Output:
Square: 9
Cube: 27
"""