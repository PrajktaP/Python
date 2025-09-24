import os

def main():
    file_name = input("Enter the name of the file that you want to ready from: ")

    if(os.path.exists(file_name)):
        print("File exists in current directory.")
        file_obj = open(file_name, "r")
        contents = file_obj.read()
        print("File contents: ", contents)

        file_obj.close()
    else:
        print("File does not exist in current directory.")

if __name__ == "__main__":
    main()



"""
2. Write a program to read and display the contents of a file data.txt.
"""