class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, otherObj):
        if self.price == otherObj.price:
            return True
        else:
            return False

def main():
    obj1_name = input("Enter name of the first Object: ")
    obj1_price = input("Enter price of the first Object: ")
    print(f"Object: {obj1_name}. Price: {obj1_price}")
    
    obj1 = Product(obj1_name, obj1_price)

    obj2_name = input("Enter name of the second Object: ")
    obj2_price = input("Enter price of the second Object: ")
    print(f"Object: {obj2_name}. Price: {obj2_price}")

    obj2 = Product(obj2_name, obj2_price)

    response = obj1.__eq__(obj2)

    if(response == True):
        print("Both Objects have same price")
    else:
        print("Both Objects have different prices")

if __name__ == "__main__":
    main()



"""
9. Create a class Product with attributes name and price. Implement __eq__ method
to compare two products if they are equal in price.
"""