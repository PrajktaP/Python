from functools import reduce

search_prime = lambda num : num % 2 == 0

def search_prime(num):
    factors = []

    for i in range(num, 0, -1):
        if((num % i) == 0):
            factors.append(i)

    return sorted(factors) == [1, num]

multiply_by_two = lambda num : num * 2

def find_max(num1, num2):
    max = num1

    if num2 > num1:
        max = num2

    return max

def main():
    # # test with hardcoded input
    # Data = [2, 70 , 11, 10, 17, 23, 31, 77]

    # accept data from user
    size = int(input("Enter number of elements: "))
    Data = []
    for i in range(size):
        Data.append(int(input("Enter a number: ")))

    print("Input list =", Data)

    filtered_data = list(filter(search_prime, Data))
    print("List after filter =", filtered_data)

    mapped_data = list(map(multiply_by_two, filtered_data))
    print("List after map =", mapped_data)

    reduced_value = reduce(find_max, mapped_data)
    print("Output of reduce =", reduced_value)

if __name__ == "__main__":
    main()



"""
5.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
"""