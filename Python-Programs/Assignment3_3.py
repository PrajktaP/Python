def main():
    size = int(input("Enter number of elements: "))

    ListOfNumbers = []
    for i in range(size):
        ListOfNumbers.append(int(input("Enter a number: ")))

    Min = ListOfNumbers[0]
    for num in ListOfNumbers:
        if num < Min:
            Min = num

    print("Numbers entered: ", ListOfNumbers)
    print("Smallest number is: ", Min)

if __name__ == "__main__":
    main()


"""
3. Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45  7
Output : 5
"""