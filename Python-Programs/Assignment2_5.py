def main():
    num = int(input("Enter a number to check if it is prime: "))

    factors = []

    for i in range(num, 0, -1):
        if((num % i) == 0):
            factors.append(i)

    if sorted(factors) == [1, num]:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is not a Prime Number")

if __name__ == "__main__":
    main()

"""
5. Write a program which accept one number for user and check whether number is prime or not.
Input : 5
Output : It is Prime Number
"""