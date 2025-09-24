# using while loop
# def sum_n(num):
#     sum = 0
#     while(num >= 1):
#         sum = sum + num
#         num = num - 1
#     return sum

# using recursive
sum = 0
def sum_n(num):
    global sum
    if(num >= 1):
        sum = sum + num
        num = num - 1
        sum_n(num)
    return sum

def main():
    input_number = int(input("Enter a number: "))
    ans = sum_n(input_number)
    print(ans)

if __name__ == "__main__":
    main()


"""
6. Sum of First N Natural Numbers
Write a recursive function to calculate sum from 1 to n.
sum_n(5) → 15
"""