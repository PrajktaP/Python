from functools import reduce

search_even = lambda num : num % 2 == 0
square = lambda num : num * num
sum = lambda num1, num2 : num1 + num2 

def main():
    # test with hardcoded input
    # Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    # accept data from user
    size = int(input("Enter number of elements: "))
    Data = []
    for i in range(size):
        Data.append(int(input("Enter a number: ")))

    print("Input list =", Data)

    filtered_data = list(filter(search_even, Data))
    print("List after filter =", filtered_data)

    mapped_data = list(map(square, filtered_data))
    print("List after map =", mapped_data)

    reduced_value = reduce(sum, mapped_data)
    print("Output of reduce =", reduced_value)

if __name__ == "__main__":
    main()



"""
4.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
"""