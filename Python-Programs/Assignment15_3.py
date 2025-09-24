import os

def main():
    contents = ""
    file_name = input("Enter the name of the file that you want to read from: ")

    response = os.path.exists(file_name)
    if(response == True): # check if the entered file exits, only then open the file and read its contents
        print("File is present in current directory")

        copy_file_obj = open(file_name, "r")
        contents = copy_file_obj.read()
        print("Contents of the file:", contents)
    else:
        print("There is no such file in current directory")

    paste_file_obj = open("Demo.txt", "w")
    paste_file_obj.write(contents)

if __name__ == "__main__":
    main()


"""
3. Write a program which accept file name from user and create new file named as Demo.txt and copy all contents from existing file into new file. 
Accept file name through command line
Input : ABC.txt
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt
"""