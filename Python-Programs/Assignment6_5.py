
def CheckPrime(Num):
    factors = []
    for i in range(Num, 0, -1):
        if((Num % i) == 0):
            factors.append(i)

    if sorted(factors) == [1, Num]:
        print(f"{Num} is a prime number.")
    else:
        print(f"{Num} is not a prime number.")

def main():
    Num = input("Enter a Number > 1: ")

    while not (Num.isnumeric() and int(Num) > 1):
        Num = input("Invalid input. Enter a Number > 1: ")

    Num = int(Num)

    if Num < 4:
        print(f"{Num} is a prime number.")
    else:
        CheckPrime(Num)

if __name__ == "__main__":
    main()


"""
Q5. Accept a number from the user and check whether it is prime or not.
Expected Input:
Enter a number: 11
Expected Output:
11 is a prime number.
"""