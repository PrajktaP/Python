power_of_two = lambda num : num ** 2

def main():
    try:
        input_number = int(input("Enter a number: "))

        resp = power_of_two(input_number)

        print(f"{input_number} raised to the power of 2 is: {resp}")
    except ValueError as vobj:
        print("Incorrect value entered: ", vobj)
    except Exception as eobj:
        print("An exception occurred: ", eobj)

if __name__ == "__main__":
    main()


"""
1.Write a program which contains one lambda function which accepts one parameter and return
power of two.
Input : 4 Output : 16
Input : 6 Output : 64
"""