# first checking using while loop
# def PrintStar(num):
#     while(num >= 1): # 4 3 2 1
#         x = 4 - (num - 1) # x = 1 2 3 4
#         for i in range(x):
#             print("*", end=" ")
#         print()
#         num = num - 1

# using recursive
def PrintStar(num):
    if(num >= 1): # 4 3 2 1
        x = 4 - (num - 1) # x = 1 2 3 4
        for i in range(x):
            print("*", end=" ")
        print()
        num = num - 1
        PrintStar(num)

def main():
    input_number = int(input("Enter a number: "))
    PrintStar(input_number)

if __name__ == "__main__":
    main()


"""
7. Print Pattern Using Recursion (Right Triangle)
Write a recursive function to print the following pattern:
*
* *
* * *
* * * *
"""