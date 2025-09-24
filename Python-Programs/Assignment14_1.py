class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Name: ", self.name)
        print("ID: ", self.emp_id)
        print("Salary: ", self.salary)

def main():
    obj = Employee('Praj', '001', 25000)
    obj.display()

if __name__ == "__main__":
    main()



"""
1. Create a class Employee with attributes name, emp_id, and salary. Create objects
of this class and print their details using a method.
Expected Output:
Name: Rohit, ID: 101, Salary: 50000
"""