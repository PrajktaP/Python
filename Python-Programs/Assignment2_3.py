def main():
    num = int(input("Enter a number: "))

    factorial = 1
    for i in range(num, 0, -1):
        factorial = factorial * i 

    print(f"Factorial of {num} is: ", factorial)

if __name__ == "__main__":
    main()


"""
3. Write a program which accept one number from user and return its factorial.
Input: 5
Output: 120
"""