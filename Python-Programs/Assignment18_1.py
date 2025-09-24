import os

def main():
    file_name = input("Enter the name of the file you want to check: ")

    if os.path.exists(file_name):
        print("File present in current directory ")
    else:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()


"""
1. Write a program which accepts file name from user and check whether that file exists in current directory or not. 
Input : Demo.txt 
Check whether Demo.txt exists or not. 
"""