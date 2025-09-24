def main():
    names = []
    try:
        count = int(input("Enter how many student names you want to enter: "))
    except ValueError as vobj:
        print("Invalid value entered | ", vobj)
        return

    file_obj = open("student.txt", "w")

    for i in range(count):
        name = input("Enter name: ")
        names.append(name)

    file_obj.write("\n".join(names))

    file_obj.close()

if __name__ == "__main__":
    main()



"""
1. Write a Python program to create a text file named student.txt and write the
names of 5 students into it.
"""