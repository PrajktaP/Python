
Area = lambda length, width :  length * width
Perimeter = lambda length, width : (2 * length) + (2 * width)

def main():
    # length = int(input("Enter Length of a rectangle: "))
    # width = int(input("Enter Width of a rectangle: "))

    while True:
        len = input("Enter Length of a rectangle: ")
        try:
            length = float(len)
            if length >= 0:
                break
            else:
                print("Length must be a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a non-negative number.")

    while True:
        wid = input("Enter Width of a rectangle: ")
        try:
            width = float(wid)
            if width >= 0:
                break
            else:
                print("Width must be a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a non-negative number.")

    area = Area(length, width)
    perimeter = Perimeter(length, width)

    print("Area of the rectangle is: ", area)
    print("Perimeter of the rectangle is: ", perimeter)

if __name__ == "__main__":
    main()


"""
Q7. Area and Perimeter of Rectangle
Accept the length and width of a rectangle. Calculate and display the area and perimeter.
Expected Input:
Enter length: 5
Enter width: 3
Expected Output:
Area: 15
Perimeter: 16
"""