
def main():
    Num = int(input("Enter a Number: "))

    for i in range(1, 11):
        print(Num * i, end=" ")

    print() # added this as it shows % at the end of output in the terminal

if __name__ == "__main__":
    main()


"""
Q3. Accept a number from the user and print its multiplication table up to 10.
Expected Input:
Enter a number: 7
Expected Output
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
"""