import os

def main():
    source_name = input("Enter the name of the file that you want to ready from: ")

    if(os.path.exists(source_name)):
        print("File exists in current directory.")
        source_file_obj = open(source_name, "r")
        contents = source_file_obj.read()
        print("File contents: ", contents)
        
        destination_name = input("Enter the name of the file that you want to write into: ")
        desti_file_obj = open(destination_name, "w")
        desti_file_obj.write(contents)

        desti_file_obj.close()
        source_file_obj.close()
    else:
        print("File does not exist in current directory.")
        exit()

if __name__ == "__main__":
    main()



"""
6. Write a Python program to copy the contents of one file (source.txt) into another
file (destination.txt).
"""