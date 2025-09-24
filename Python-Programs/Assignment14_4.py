class Student:
    school_name = "GGIS"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("School name:", Student.school_name)
        print("Student name:", self.name)
        print("Student roll no: ", self.roll_no)

def main():
    obj = Student('Praj', '10')
    obj.display()

    Student.school_name = "ABC"

    print("Updated school name:", Student.school_name)

if __name__ == "__main__":
    main()



"""
4. Create a class Student with name, roll_no, and a class variable school_name. Print
student details and school name. Change the school name using class name.
"""