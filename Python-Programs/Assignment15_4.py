import os

def main():
    contents1 = ""
    file1_name = input("Enter the name of First file: ")

    response = os.path.exists(file1_name)
    if(response == True): # check if the entered file exits, only then open the file and read its contents
        print("File is present in current directory")

        file1_obj = open(file1_name, "r")
        contents1 = file1_obj.read()
        print("Contents of the file:", contents1)
    else:
        print(f"There is no such file named {file1_name} in current directory")
        return

    contents2 = ""
    file2_name = input("Enter the name of Second file: ")

    response = os.path.exists(file2_name)
    if(response == True): # check if the entered file exits, only then open the file and read its contents
        print("File is present in current directory")

        file2_obj = open(file2_name, "r")
        contents2 = file2_obj.read()
        print("Contents of the file:", contents2)
    else:
        print(f"There is no such file named {file2_name} in current directory")
        return
    
    # program would return if any of the above files are not existing. 
    # following code will continue only if both files exist

    if contents1 == contents2:
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()


"""
4. Write a program which accept two file names from user and compare contents of both the files.
If both the files contains same contents then display success otherwise display failure.
Accept names of both the files from command line.
"""