import os

def main():
    file_name = input("Enter the name of the file you want to read from: ")

    if os.path.exists(file_name):
        print("File present in current directory ")
    else:
        print("File is not present in current directory")

    fobj = open(file_name, "r")
    contents = fobj.read()

    fobj2 = open("Demo.txt", "w")
    fobj2.write(contents)

    fobj.close()
    fobj2.close()

if __name__ == "__main__":
    main()


"""
3. Write a program which accept file name from user and create new file named as Demo.txt and 
copy all contents from existing file into new file. Accept file name through command line 
Input : ABC.txt 
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt 
"""