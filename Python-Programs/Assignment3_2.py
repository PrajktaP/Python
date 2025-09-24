def main():
    size = int(input("Enter number of elements: "))

    ListOfNumbers = []
    for i in range(size):
        ListOfNumbers.append(int(input("Enter a number: ")))

    Max = 0
    for num in ListOfNumbers:
        if num > Max:
            Max = num

    print("Numbers entered: ", ListOfNumbers)
    print("Biggest number is: ", Max)

if __name__ == "__main__":
    main()


"""
2. Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
Input: Number of elements: 7
Input Elements : 13 5 45 7 4 56 34
Output : 56
"""