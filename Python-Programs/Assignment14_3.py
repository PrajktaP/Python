class Book:
    def __init__(self, price):
        self.__price = price
    
    def getPrice(self):
        return self.__price
    
    def setPrice(self, price):
        self.__price = price

def main():
    try:
        price = float(input("Enter the price of the book:"))

        obj = Book(price)

        print("Current price of the book is:", obj.getPrice())

        new_price = float(input("Enter the new price of the book:"))

        obj.setPrice(new_price)

        print("Updated price of the book is:", obj.getPrice())
    except ValueError as vobj:
        print("Invalid value entered", vobj)
    except Exception as eobj:
        print("Exception occurred", eobj)

if __name__ == "__main__":
    main()



"""
3. Create a class Book with private attribute __price. Add methods to get and set the
price. Show encapsulation.
"""