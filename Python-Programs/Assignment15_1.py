import os

def main():
    file_name = input("Enter the name of the file that you want to check if exists: ")

    response = os.path.exists(file_name)

    if(response == True):
        print("File is present in current directory")
    else:
        print("There is no such file in current directory")

if __name__ == "__main__":
    main()


"""1. Write a program which accepts file name from user and check whether that file exists in current directory or not."""