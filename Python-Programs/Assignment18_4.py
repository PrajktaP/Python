import os
import sys

def main():
    if len(sys.argv) < 3:
        print("Invalid arguments. You need to pass both file names.")
        print("Command should look something like: python assignment_name.py file1.txt file2.txt")
        exit()

    file_name_first = sys.argv[1]
    file_name_second = sys.argv[2]

    if not os.path.exists(file_name_first):
        print(f"File {file_name_first} is not present in current directory")
        exit()

    if not os.path.exists(file_name_second):
        print(f"File {file_name_second} is not present in current directory")
        exit()

    fobj_first = open(file_name_first, "r")
    contents_first = fobj_first.read()

    fobj_second = open(file_name_second, "r")
    contents_second = fobj_second.read()

    if contents_first == contents_second:
        print("Success")
    else:
        print("Failure")

    fobj_first.close()
    fobj_second.close()

if __name__ == "__main__":
    main()


"""
4. Write a program which accept two file names from user and compare contents of both the files. 
If both the files contains same contents then display success otherwise display failure. 
Accept names of both the files from command line. 
Input: Demo.txt Hello.txt 
Compare contents of Demo.txt and Hello.txt 
"""