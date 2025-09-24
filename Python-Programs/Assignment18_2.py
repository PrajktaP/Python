import os

def main():
    file_name = input("Enter the name of the file you want to read from: ")

    if os.path.exists(file_name):
        print("File present in current directory ")
    else:
        print("File is not present in current directory")

    fobj = open(file_name, "r")

    contents = fobj.read()

    print("Below are the contents of the file: \n")
    print(contents)

    fobj.close()

if __name__ == "__main__":
    main()


"""
2. Write a program which accept file name from user and open that file and display the contents of that file on screen. 
Input : Demo.txt 
Display contents of Demo.txt on console. 
"""