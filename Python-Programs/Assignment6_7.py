
def main():
    print("Enter 5 numbers: ")

    Data = []

    for i in range(5):
        Data.append(int(input()))

    print("Numbers entered: ", Data)

    Max = Data[0]
    for num in Data:
        if num > Max:
            Max = num

    print("Maximum number is: ", Max)

if __name__ == "__main__":
    main()


"""
Q7. Accept 5 numbers from the user. Find and print the largest number.
Expected Input:
Enter 5 numbers: 23 89 12 56 45
Expected Output:
Maximum number is: 89
"""