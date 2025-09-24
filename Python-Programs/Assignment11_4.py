# using resursion
pow = 1
i = 1
def Power(num1, num2):
    global pow
    global i
    if(i <= num2): # 1 <= 3, 2 <= 3, 3 <= 3
        pow = pow * num1 # 1 * 2 = 2, 2 * 2 = 4, 4 * 2 = 8
        i = i + 1
        Power(num1, num2)
    return pow

def main():
    input_num1 = int(input("Enter first number: "))
    input_num2 = int(input("Enter second number: "))
    pow = Power(input_num1, input_num2)

    print(f"Power ({input_num1}, {input_num2}): ", pow)

if __name__ == "__main__":
    main()


"""
4. Power Function Using Recursion
Write a recursive function to calculate x^n.
power(2, 3) → 8
"""