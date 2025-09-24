def main():
    num1 = int(input("Enter a number: "))
    
    for i in range(num1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print("\n")

if __name__ == "__main__":
    main()


"""
6. Write a program which accept one number and display below pattern.
Input :5

Output:
* * * * *
* * * * 
* * * 
* *
*
"""