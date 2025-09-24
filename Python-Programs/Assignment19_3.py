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
    
    if not os.path.exists(desti_dir_name):
        os.mkdir(desti_dir_name)

    # get absolute path of the directory name passed in as second argument
    abs_dir_path = os.path.abspath(source_dir_name)

    # check if the directory exists
    is_dir = os.path.isdir(abs_dir_path)
    if not is_dir:
        print(f"Directory '{abs_dir_path}' does not exist.")
        return

    # Copy each file from source to destination
    for item in os.listdir(source_dir_name):
        src_path = os.path.join(source_dir_name, item)
        dst_path = os.path.join(desti_dir_name, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)  # copy2 preserves metadata from source file, copy does not.. data like timestamps
            print(f"Copied: {item}")

if __name__ == "__main__":
    main()



"""
3. Design automation script which accept two directory names. Copy all files from first directory into second directory. 
Second directory should be created at run time. 
Usage : DirectoryCopy.py 'Demo' 'Temp' 
Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and 
copy all files from Demo to Temp. 

> python Assignment19_3.py 'Demo' 'Temp'
"""

"""
shutil.copy2 preserves metadata
will silently overwrite the existing file at dst_path — without warning, and:
It will replace the file contents with the source file’s contents.
It will also overwrite the file’s metadata (timestamps, etc.) to match the source.
"""