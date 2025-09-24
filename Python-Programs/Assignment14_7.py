class Person:
    def __init__(self, name, age):
        print("Inside Person Constructor")
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, sub, sal):
        print("Inside Teacher Constructor")
        self.subject = sub
        self.salary = sal
        super().__init__(name, age)


def main():
    obj = Teacher('Praj', '35', 'Maths', '40000')

    print("name:",obj.name)
    print("age:",obj.age)
    print("subject:",obj.subject)
    print("salary:",obj.salary)

if __name__ == "__main__":
    main()



"""
7. Create a base class Person with name and age. Derive a class Teacher with subject
and salary. Use super() to call base class constructor and print both.
"""