
Even = lambda num : num % 2 == 0

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    for i in range(size):
        Data.append(int(input("Enter a number: ")))

    print("Entered list: ", Data)

    # -- without filter function
    EvenData = []
    for num in Data:
        if Even(num):
            EvenData.append(num)
    print("Entered list: ", EvenData)

    # -- using filter function
    FEvenData = list(filter(Even, Data))
    print("Even numbers: ", FEvenData)

if __name__ == "__main__":
    main()


"""
Q3. Accept a list of numbers and use filter() to keep only even numbers.
Expected Input:
Enter list: 1 2 3 4 5 6
Expected Output:
Even numbers: [2, 4, 6]
"""