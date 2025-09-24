def main():
    num1 = int(input("Enter a number: "))
    
    for i in range(num1):
        for j in range(1, num1+1):
            print(j, end=" ")
        print("\n")

if __name__ == "__main__":
    main()


"""
7. Write a program which accept one number and display below pattern.
Input :5

Output:
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""