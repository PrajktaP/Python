def CheckDivisibilityBy5():
    value = int(input("Enter a number: "))

    if value % 5 == 0:
        return True
    else:
        return False

response = CheckDivisibilityBy5()
print(response)


"""
7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
Input : 8                   Output : False
Input : 25                  Output : True
"""