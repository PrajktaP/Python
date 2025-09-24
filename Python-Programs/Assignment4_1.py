Power = lambda x : x ** 2

def main():
    num = int(input("Enter a number: "))

    # Find Power of the number
    Ans = Power(num)
    print(f"Power of {num} is: ", Ans)

if __name__ == "__main__":
    main()


"""
1. Write a program which contains one lambda function which accepts one parameter and return power of two.
Input : 4     Output : 16
Input : 6     Output : 64
"""