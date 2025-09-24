from functools import reduce

Product = lambda num1, num2 : num1 * num2

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    for i in range(size):
        Data.append(int(input("Enter a number: ")))

    print("Entered list: ", Data)

    # -- without reduce function
    ProductAns = 1
    for num in Data:
        ProductAns = ProductAns * num
    print("Product: ", ProductAns)

    # -- using reduce function
    RProductAns = int(reduce(Product, Data))
    print("Product using reduce function: ", RProductAns)

if __name__ == "__main__":
    main()

"""
Q4. Accept a list of numbers and use reduce() (from functools) to find the product of
all numbers.
Expected Input:
Enter list: 2 3 4
Expected Output:
Product: 24
"""