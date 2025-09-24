import os

def main():
    file_name = input("Enter the name of the file that you want to read from: ")

    response = os.path.exists(file_name)

    if(response == True): # check if the entered file exits, only then open the file and read its contents
        print("File is present in current directory")

        file_obj = open(file_name, "r")
        contents = file_obj.read()
        print("Contents of the file:", contents)

    else:
        print("There is no such file in current directory")

if __name__ == "__main__":
    main()


"""
2. Write a program which accept file name from user and open that file and display the contents of that file on screen.
Input : Demo.txt
Display contents of Demo.txt on console.
"""