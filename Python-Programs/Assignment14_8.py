class Vehicle:
    def __init__(self):
        print("Inside Vehicle's constructor")

    def start(self):
        print("Starting Vehicle...")

class Car(Vehicle):
    def __init__(self):
        print("Inside Car's constructor")
        super().__init__()

    def start(self):
        print("Starting Car...")

def main():
    cobj = Car()
    cobj.start()

if __name__ == "__main__":
    main()


"""
8. Create a class Vehicle with method start(). Derive class Car and override the
method start() with additional behavior. Show method overriding.
"""