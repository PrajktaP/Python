import os

def main():
    file_name = input("Enter the name of the file that you want to read from: ")

    response = os.path.exists(file_name)

    if(response == True): # check if the entered file exits, only then open the file and read its contents
        print("File is present in current directory")

        file_obj = open(file_name, "r")
        contents = file_obj.read()
        print("Contents of the file:", contents)

        search_string = input("Enter a word that you want to search in this file: ")
        count = contents.lower().count(search_string.lower())  # Case-insensitive search count
        print(f"The word '{search_string}' appears {count} times.")

    else:
        print("There is no such file in current directory")

if __name__ == "__main__":
    main()



"""
5. Accept file name and one string from user and return the frequency of that string from file.
Input : Demo.txt
Marvellous
Search "Marvellous" in Demo.txt
"""