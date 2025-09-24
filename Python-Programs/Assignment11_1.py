# check using while loop first
# def display(n):
#     i = 1
#     while(i <= n):
#         print(i, end=" ")
#         i = i + 1
#     print()

# using resursion
i = 1
def display(n):
    global i
    if(i <= n):
        print(i, end=" ")
        i = i + 1
        display(n)

def main():
    input_number = int(input("Enter a number: "))
    display(input_number)

if __name__ == "__main__":
    main()

"""
1. Print Numbers Using Recursion
Write a recursive function to print numbers from 1 to N.
Expected Output (for n=5):
1 2 3 4 5
"""