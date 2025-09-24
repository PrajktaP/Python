
def CheckPallindrome(Str):
    asc = []
    for char in Str:
        asc.append(char)
    print("String in normal order: ", asc)

    desc = []
    for i in range(len(Str) - 1, -1, -1):
        desc.append(Str[i])
    print("String in reverse order: ", desc)

    # if string in normal order and string in reverse order are same
    if asc == desc:
        print(f"{Str} is pallindrome")
    else:
        print(f"{Str} is not a pallindrome")


def main():
    Str = input("Enter a string: ")

    CheckPallindrome(Str)

if __name__ == "__main__":
    main()

"""
Q5. Write a function that accepts a string and checks whether it is a palindrome.
Expected Input:
Enter a string: radar
Expected Output:
radar is a palindrome.
"""