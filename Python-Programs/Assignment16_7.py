def main():
    # read student_marks.txt file
    file_obj = open("student_marks.txt", "r")
    lines = file_obj.readlines()

    for line in lines:
        words = line.split() # default is split on whitespace
        if len(words) == 2:
            marks = words[1]
            if(int(marks) > 75):
                print(f"Name: {words[0]}. Marks: {words[1]}")

if __name__ == "__main__":
    main()



"""
7. Create a file marks.txt with student name and marks. Then read the file and
display students who scored more than 75 marks.
"""

"""
used following code to enter student details like name and marks format

students = []
try:
    count = int(input("Enter how many student details you want to enter: "))
except ValueError as vobj:
    print("Invalid value entered | ", vobj)
    return

# write the student name and marks in the student_marks.txt file
file_obj = open("student_marks.txt", "w")
for i in range(count):
    name = input("Enter name: ")
    try:
        marks = int(input("Enter marks: "))
        students.append(name + " " + str(marks))
    except ValueError as vobj:
        print("Invalid value for marks entered | ", vobj)
        exit()
file_obj.write("\n".join(students))
file_obj.close()
"""