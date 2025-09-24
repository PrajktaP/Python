import os
import sys
import shutil

def main():
    args = sys.argv
    if(len(args) < 3):
        print("Invalid arguments")
        exit()
    
    source_dir_name = args[1]
    desti_dir_name = args[2]
    extension = args[3]
    
    if not os.path.exists(desti_dir_name):
        os.mkdir(desti_dir_name)

    # get absolute path of the directory name passed in as second argument
    abs_dir_path = os.path.abspath(source_dir_name)

    # check if the directory exists
    is_dir = os.path.isdir(abs_dir_path)
    if not is_dir:
        print(f"Directory '{abs_dir_path}' does not exist.")
        return

    # Copy files with passed in extension, from source to destination folder
    for item in os.listdir(source_dir_name):
        src_path = os.path.join(source_dir_name, item)
        dst_path = os.path.join(desti_dir_name, item)

        print("item:", item)

        file_ext = item.split(".")[1]
        print("file_ext:", file_ext)

        if os.path.isfile(src_path) and (file_ext == extension):
            shutil.copy(src_path, dst_path)  # copy2 preserves metadata from source file, copy does not.. data like timestamps
            print(f"Copied: {item}")

if __name__ == "__main__":
    main()



"""
4. Design automation script which accept two directory names and one file extension. 
Copy all files with the specified extension from first directory into second directory. 
Second directory should be created at run time. 
Usage : DirectoryCopyExt.py 'Demo' 'Temp' '.exe' 
Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and 
copy all files with extension .exe from Demo to Temp.

> python Assignment19_4.py 'Demo' 'Temp2' 'py'
"""