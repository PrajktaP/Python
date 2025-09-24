from functools import reduce

# functions
def CheckPrime(num):
    factors = []

    for i in range(num, 0, -1):
        if((num % i) == 0):
            factors.append(i)

    return sorted(factors) == [1, num]

MultiplyByTwo = lambda num : num * 2

def FindMax(num1, num2):
    max = num1

    if num2 > num1:
        max = num2

    return max

# Logic
def main():
    # Data = [2, 70, 11, 10, 17, 23, 31, 77]

    size = int(input("Enter number of elements: "))

    Data = []
    for i in range(size):
        Data.append(int(input("Enter a number: ")))

    print("Input data: ", Data)

    FData = list(filter(CheckPrime, Data))
    print("Filter output: ", FData)

    MData = list(map(MultiplyByTwo, FData))
    print("Map output: ", MData)

    RData = reduce(FindMax, MData)
    print("Reduce output: ", RData)

if __name__ == "__main__":
    main()


"""
5. Write a program which contains filter(), map() and reduce) in it. Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. 
Filter should filter out all prime numbers. 
Map function will multiply each number by 2. 
Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
Input List = [2, 70, 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
"""