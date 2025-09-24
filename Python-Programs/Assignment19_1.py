import os
import sys

def main():
    args = sys.argv
    if(len(args) < 3):
        print("Invalid arguments")
        exit()
    
    dir_name = args[1]

    # get absolute path of the directory name passed in as second argument
    abs_dir_path = os.path.abspath(dir_name)

    # check if the directory exists
    is_dir = os.path.isdir(abs_dir_path)
    if not is_dir:
        print(f"Directory '{abs_dir_path}' does not exist.")
        return

    # argument 3 is the file extension
    ext = args[2]
    directory_listing = os.scandir(abs_dir_path)
    for item in directory_listing:
        if item.is_file() and item.name.endswith(ext):
            print(item.name)

if __name__ == "__main__":
    main()


"""
1. Design automation script which accept directory name and file extension from user. Display all files with that extension. 
Usage : DirectoryFileSearch.py 'Demo' '.txt' 
Demo is name of directory and txt is the extension that we want to search. 

> python Assignment19_1.py 'Demo' '.txt'
"""