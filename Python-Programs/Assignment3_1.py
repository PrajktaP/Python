def main():
    size = int(input("Enter number of elements: "))

    ListOfNumbers = []
    for i in range(size):
        ListOfNumbers.append(int(input("Enter a number: ")))

    Addition = 0
    for num in ListOfNumbers:
        Addition = Addition + num

    print("Numbers entered: ", ListOfNumbers)
    print("Addition of all these numbers: ", Addition)

if __name__ == "__main__":
    main()

"""
1. Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4  56
Output : 130
"""