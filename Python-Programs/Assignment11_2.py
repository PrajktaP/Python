# using resursion
fact = 1
def factorial(num):
    global fact
    if(num >= 1):
        fact = fact * num
        num = num - 1
        factorial(num)
    return fact

def main():
    input_number = int(input("Enter a number: "))
    fact = factorial(input_number)

    print(f"Factorial for {input_number}: ", fact)

if __name__ == "__main__":
    main()

"""
2. Factorial Using Recursion
Write a recursive function to calculate factorial of a number.
factorial(5) → 120
"""