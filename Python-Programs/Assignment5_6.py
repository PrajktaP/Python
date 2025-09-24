
def CelsToFahr(Cels):
    Fahr = (Cels * 9/5) + 32

    return Fahr

def main():
    while True:
        Cels = input("Enter temperature in Celsius: ")
        try:
            num = float(Cels)  # to Accept both integer and float
            break  # Valid number, break the loop
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    TempInFahr = CelsToFahr(num)

    print(f"Temperature in Fahrenheit: {TempInFahr}°F")

if __name__ == "__main__":
    main()


"""
Q6. Celsius to Fahrenheit Converter
Accept temperature in Celsius and convert it to Fahrenheit using the formula:
F = (C * 9/5) + 32
Expected Input:
Enter temperature in Celsius: 25
Expected Output:
Temperature in Fahrenheit: 77.0°F
"""