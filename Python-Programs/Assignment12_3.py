class Arithmetic:
    def __init__(self):
        print("Inside constructor")
        self.value1 = 0
        self.value2 = 0

    def accept(self):
        try:
            value1 = int(input("Enter first number: "))
            value2 = int(input("Enter second number: "))
            return value1, value2
        except ValueError as vobj:
            print("Invalid input! Please enter numeric values.", vobj)

    def addition(self, value1, value2):
        ans = value1 + value2
        return ans

    def subtraction(self, value1, value2):
        ans = value1 - value2
        return ans

    def multiplication(self, value1, value2):
        ans = value1 * value2
        return ans

    def division(self, value1, value2):
        ans = value1 / value2
        return ans
    
    def __del__(self):
        print("Inside destructor")

def main():
    obj = Arithmetic()
    value1, value2 = obj.accept()

    add = obj.addition(value1, value2)
    print("Addition result is: ", add)

    sub = obj.subtraction(value1, value2)
    print("Subtraction result is: ", sub)

    multi = obj.multiplication(value1, value2)
    print("Multiplication result is: ", multi)

    div = obj.division(value1, value2)
    print("Division result is: ", div)

if __name__ == "__main__":
    main()



"""
3. Write a program which contains one class named as c.
Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.
"""