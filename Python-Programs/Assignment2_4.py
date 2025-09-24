def main():
    num = int(input("Enter a number: "))

    Addition = 0
    factors = []

    for i in range(num, 0, -1):
        if((num % i) == 0):
            factors.append(i)
            Addition = Addition + i

    print("Factors are: ", factors)
    print(f"Addition of factors of {num} is: ", Addition)

if __name__ == "__main__":
    main()

"""
4. Write a program which accept one number form user and return addition of its factors.
Input : 12
Output : 16 (1+2+3+4+6)
"""