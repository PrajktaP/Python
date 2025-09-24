def addition(data):
    sum = 0
    for value in data:
        sum = sum + value
    return sum

def display(data):
    print("Entered elements are: ")
    for value in data:
        print(value)

def findOddEven(data):
    odds = []
    evens = []
    for value in data:
        if value % 2 == 0:
            evens.append(value)
        else:
            odds.append(value)
    return odds,evens

def main():
    size = int(input("Enter number of elements: "))

    data = list()

    print("Enter the values")

    for i in range(1, size+1):
        no = int(input(f"Enter value {i}: "))
        data.append(no)
    
    # display entered numbers
    display(data)

    # find the addition of entered numbers
    sum = addition(data)
    print("Addition is: ", sum)

    # Identify the odd and even numbers
    odds,evens = findOddEven(data)
    print("Odd numbers: ", odds)
    print("Even numbers: ", evens)

if __name__ == "__main__":
    main()

# Ask user how many numbers they want to enter
# get those many numbers from the User
# display the entered numbers
# display addition
# display odd even values