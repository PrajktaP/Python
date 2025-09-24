
def CheckIfVowel(Char):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if Char in vowels:
        print(f"{Char} is a vowel.")
    else:
        print(f"{Char} is a consonant.")


def main():
    char = input("Enter a character: ")

    while len(char) != 1 or not char.isalpha():
        char = input("Invalid input. Enter a single alphabet character: ")

    CheckIfVowel(char)

if __name__ == "__main__":
    main()

"""
Q2. Vowel or Consonant Check
Accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not, print it's a consonant.

Expected Input:
Enter a character: e
Expected Output: 'e' is a vowel.
"""