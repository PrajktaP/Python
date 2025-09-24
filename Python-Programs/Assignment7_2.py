
Double = lambda num : num * 2

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    for i in range(size):
        Data.append(int(input("Enter a number: ")))
    
    print("Entered list: ", Data)

    # -- without map function
    DoubledData = []
    for num in Data:
        DoubledData.append(Double(num))
    print("Doubled list: ", DoubledData)

    # -- using map function
    MDoubledData = list(map(Double, Data))
    print("Doubled list using map method: ", MDoubledData)

if __name__ == "__main__":
    main()


"""
Q2. Accept a list of integers from the user and use the map() function to double each
value.
Expected Input:
Enter list: 1 2 3 4 5
Expected Output:
Doubled list: [2, 4, 6, 8, 10]
"""