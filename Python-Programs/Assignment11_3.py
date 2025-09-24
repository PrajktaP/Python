# using resursion
sum = 0
i = 0
def SumOfDigits(num):
    global sum
    global i
    if(i < len(num)):
        sum = sum + int(num[i])
        i = i + 1
        SumOfDigits(num)
    return sum

def main():
    input_number = input("Enter a number: ")
    sum = SumOfDigits(input_number)

    print(f"Sum Of the Digits of {input_number}: ", sum)

if __name__ == "__main__":
    main()

"""
3. Sum of Digits
Write a recursive function to calculate the sum of digits of a number.
sum_of_digits(1234) → 10
"""