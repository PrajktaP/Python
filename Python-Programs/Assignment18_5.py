import os
import sys

def main():
    if len(sys.argv) < 3:
        print("Invalid arguments. You need to pass both file names.")
        print("Command should look something like: python assignment_name.py file.txt search_key")
        exit()

    file_name = sys.argv[1]

    if not os.path.exists(file_name):
        print(f"File {file_name} is not present in current directory")
        exit()

    fobj = open(file_name, "r")
    contents = fobj.read()

    search_key = sys.argv[2]

    count = contents.count(search_key)
    print(f"Word '{search_key}' occurs {count} times in {file_name} file.")

    fobj.close()

if __name__ == "__main__":
    main()


"""
5. Accept file name and one string from user and return the frequency of that string from file. 
Input : Demo.txt Marvellous. Search 'Marvellous' in Demo.txt 
"""