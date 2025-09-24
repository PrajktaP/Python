class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

def main():
    try:
        len = int(input("Enter the length: "))
        wid = int(input("Enter the width: "))

        obj = Rectangle(len, wid)

        ar = obj.area()
        print("Area: ", ar)

        peri = obj.perimeter()
        print("Perimeter: ", peri)
    except ValueError as vobj:
        print("Invalid input", vobj)
    except Exception as eobj:
        print("Exception Occurred", eobj)

if __name__ == "__main__":
    main()



"""
2. Write a class Rectangle with length and width. Add a method to compute area and
perimeter.
Area: 50, Perimeter: 30
"""