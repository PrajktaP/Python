import os
import sys

def main():
    args = sys.argv
    if(len(args) < 4):
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
    new_ext = args[3]  # new extension
    for old_file_name in os.listdir(abs_dir_path):
        base, old_file_ext = os.path.splitext(old_file_name)
        print("base:",base)
        print("old_file_ext:",old_file_ext)

        if old_file_ext == ext:
            old_path = os.path.join(abs_dir_path, old_file_name)

            new_file_name = base + new_ext
            new_path = os.path.join(abs_dir_path, new_file_name)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {old_file_name} to {new_file_name}")

if __name__ == "__main__":
    main()



"""
2. Design automation script which accept directory name and two file extensions from user. 
Rename all files with first file extension with the second file extention. 
Usage : DirectoryRename.py 'Demo''.txt' '.doc' 
Demo is name of directory and txt is the extension that we want to search and rename with .doc. 
After execution this script each txt file gets renamed as .doc. 

> python Assignment19_2.py 'Demo' '.txt' '.doc'
"""


# # argument 3 is the file extension
# ext = args[2]
# new_ext = args[3]  # new extension
# directory_listing = os.scandir(abs_dir_path)
# for item in directory_listing:
#     if item.is_file() and item.name.endswith(ext):
#         print(item.name)
#         # Split name and extension ex. "text.txt" -> ['text','txt']
#         base = item.name.split('.')[0] # 'text'
#         new_file_name = base + new_ext

#         old_path = item.path  # full path to original file
#         new_path = os.path.join(abs_dir_path, new_file_name)  # full path for new file

#         # Rename the file
#         os.rename(old_path, new_path)
#         print(f"Renamed: {item.name} to {new_file_name}")