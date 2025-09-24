from functools import reduce

# lambda functions
FindEven = lambda num : num % 2 == 0
FindSqaure = lambda num : num * num
Addition = lambda num1, num2 : num1 + num2 

# Logic
def main():
    # Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    size = int(input("Enter number of elements: "))

    Data = []
    for i in range(size):
        Data.append(int(input("Enter a number: ")))

    print("Input data: ", Data)

    FData = list(filter(FindEven, Data))
    print("Filter output: ", FData)

    MData = list(map(FindSqaure, FData))
    print("Map output: ", MData)

    RData = reduce(Addition, MData)
    print("Reduce output: ", RData)

if __name__ == "__main__":
    main()


"""
4. Write a program which contains filter), map() and reduce() in it. Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. 
Filter should filter out all such numbers which are even. 
Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
"""