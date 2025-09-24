from functools import reduce

# lambda functions
Search = lambda num : num >= 70 and num <= 90
IncreaseByTen = lambda num : num + 10
Product = lambda num1, num2 : num1 * num2 

# Logic
def main():
    # Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    size = int(input("Enter number of elements: "))

    Data = []
    for i in range(size):
        Data.append(int(input("Enter a number: ")))

    print("Input data: ", Data)

    FData = list(filter(Search, Data))
    print("Filter output: ", FData)

    MData = list(map(IncreaseByTen, FData))
    print("Map output: ", MData)

    RData = reduce(Product, MData)
    print("Reduce output: ", RData)

if __name__ == "__main__":
    main()

"""
3. Write a program which contains filter(), map() and reduce) in it. Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. 
Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. 
Map function will increase each number by 10. 
Reduce will return product of all that numbers.

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000
"""