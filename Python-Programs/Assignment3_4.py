def main():
    size = int(input("Enter number of elements: "))

    ListOfNumbers = []
    DictOfNumbers = {}
    for i in range(size):
        inputNumber = int(input("Enter a number: "))

        ListOfNumbers.append(inputNumber)

        if inputNumber not in DictOfNumbers:
            DictOfNumbers[inputNumber] = 0

        DictOfNumbers[inputNumber] = DictOfNumbers[inputNumber] + 1

    print("Numbers you entered are: ", ListOfNumbers)

    numberToFind = int(input("Enter any number from the numbers you entered: "))
    if numberToFind not in DictOfNumbers:
        print(f"Number of times {numberToFind} occurs is: 0")
    else:
        print(f"Number of times {numberToFind} occurs is: ", DictOfNumbers[numberToFind])

if __name__ == "__main__":
    main()


"""
Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number 
from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3
"""