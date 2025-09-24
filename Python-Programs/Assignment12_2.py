class Circle:
    pi = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0
    
    def accept(self):
        try:
            radius = float(input("Enter the radius of the circle: "))
            return radius
        except ValueError as vobj:
            print("Invalid input! Please enter numeric values.", vobj)

    def calculate_area(self, radius):
        area = Circle.pi * radius * radius
        return area

    def calculate_circumference(self, radius):
        circumference = 2 * Circle.pi * radius
        return circumference

    def display(self, radius, area, circumference):
        print("Radius is: ", radius)
        print("Area is: ", area)
        print("Circumference is: ", circumference)

def main():
    cObj1 = Circle()

    radius = cObj1.accept()
    area = cObj1.calculate_area(radius)
    circumference = cObj1.calculate_circumference(radius)
    cObj1.display(radius, area, circumference)

    cObj2 = Circle()

    radius = cObj2.accept()
    area = cObj2.calculate_area(radius)
    circumference = cObj2.calculate_circumference(radius)
    cObj2.display(radius, area, circumference)

if __name__ == "__main__":
    main()


"""
2. Write a program which contains one class named as Circle.
Circle class contains three instance variables as Radius ,Area, Circumference.
That class contains one class variable as PI which is initialise to 3.14.
Inside init method initialise all instance variables to 0.0.
There are three instance methods inside class as Accept(), CalculateArea, CalculateCircumference(), Display(). 
Accept method will accept value of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable Area.
CalculateCircumference() method will calculate circumference of circle and store it into instance
variable Circumference.
And Display() method will display value of all the instance variables as Radius , Area,
Circumference.
After designing the above class call all instance methods by creating multiple objects.
"""