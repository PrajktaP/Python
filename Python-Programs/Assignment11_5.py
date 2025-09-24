i = 0
total_zeros = 0
def CountZeros(num):
    global i
    global total_zeros
    if(i < len(num)):
        if num[i] == "0":
            total_zeros = total_zeros + 1
        i = i + 1
        CountZeros(str(num))
    return total_zeros

def main():
    input_number = input("Enter a number: ")
    total_zeros = CountZeros(input_number)
    print("Total number of 0's:", total_zeros)

if __name__ == "__main__":
    main()


"""
5. Count Zeros in a Number (Recursively)
Write a recursive function to count how many zeros are in the given number.
count_zeros(1020300) → 4
"""