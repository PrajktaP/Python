class Employee:
    def __init__(self, name, sal, dept):
        print("Employee init")
        self.name = name
        self._department = dept # protected attribute
        self.__salary = sal # private attribute
    
    def display(self):
        print("Name: ", self.name)
        print("Department: ", self._department)
        print("Salary: ", self.__salary)

class Developer(Employee):
    def __init__(self, name, sal, dept, years):
        print("Developer init")
        super().__init__(name, sal, dept)
        self.exp_in_years = years

    def display(self):
        print("Name: ", self.name)
        print("Department: ", self._department) # protected attribute accessible in child class
        # print("Salary: ", self.__salary) # not accessible
        print("Experience In Years: ", self.exp_in_years)

def main():
    eobj = Employee('Praj', '50000', 'Collections')
    eobj.display()

    dobj = Developer('Rohit', '45000', 'IT', 3)
    dobj.display()

if __name__ == "__main__":
    main()


"""
10. Demonstrate private, protected and public access modifiers using a class Employee
with attributes: __salary, _department, name.
"""