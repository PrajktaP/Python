
def main():
    Data = []

    print("Enter 3 numbers")

    for i in range(3):
        Data.append(int(input()))

    print("Input data: ", Data)

    Max = Data[0]
    for i in Data:
        if i > Max:
            Max = i

    print("Max number is: ", Max)

if __name__ == "__main__":
    main()


"""
Q4. Find Largest Among Three Numbers
Accept three numbers from the user and print the largest using nested if-else statements.
Expected Input:
Enter three numbers: 5 9 3
Expected Output:
Largest number is 9.
"""