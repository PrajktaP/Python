def main():
    num1 = int(input("Enter a number: "))
    
    for i in range(num1):
        for j in range(num1):
            print("*", end=" ")
        print("\n")

if __name__ == "__main__":
    main()


"""
2. Write a program which accept one number and display below pattern.
Input :5

Output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""