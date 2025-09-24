
def main():
    Num = int(input("Enter a Number: "))

    Factorial = 1
    for i in range(Num, 1, -1):
        Factorial = Factorial * i

    print(f"Factorial of {Num} is", Factorial)

if __name__ == "__main__":
    main()


"""
Q4. Accept a number and print its factorial using a for loop.
Expected Input:
Enter a number: 5
Expected Output:
Factorial of 5 is: 120
"""