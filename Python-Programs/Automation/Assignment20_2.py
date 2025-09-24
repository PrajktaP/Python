import os
import sys
import time
import hashlib

def calculateChecksum(path, blocksize = 1024):
    fobj = open(path, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(blocksize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(blocksize)

    fobj.close()

    return hobj.hexdigest()

def directory_watcher(dir_name = "Marvellous"):
    flag = os.path.isabs(dir_name)

    if(flag == False):
        dir_name = os.path.abspath(dir_name)

    flag = os.path.exists(dir_name)
    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(dir_name)
    if(flag == False):
        print(f"Path is valid, but target is not a directory")
        exit()

    for folder_name, sub_folder_names, file_names in os.walk(dir_name):
        for fname in file_names:
            fname = os.path.join(folder_name, fname)
            check_sum = calculateChecksum(fname)
            print(f"Filename: {fname}. Checksum: {check_sum}.")
            print()

def log_duplicate(file_name):
    mode = "w"
    if(os.path.exists("FileActivity.log")):
        mode = "a"
    else:
        mode = "w"
    fobj = open("FileActivity.log", mode)

    fobj.write(f"{file_name} \n")

def find_duplicate(dir_name = "Marvellous"):
    flag = os.path.isabs(dir_name)

    if(flag == False):
        dir_name = os.path.abspath(dir_name)

    flag = os.path.exists(dir_name)
    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(dir_name)
    if(flag == False):
        print(f"Path is valid, but target is not a directory")
        exit()

    duplicate = {}
    for folder_name, sub_folder_names, file_names in os.walk(dir_name):
        for fname in file_names:
            fname = os.path.join(folder_name, fname)
            check_sum = calculateChecksum(fname)
            if(check_sum in duplicate):
                duplicate[check_sum].append(fname)
                log_duplicate(fname)
            else:
                duplicate[check_sum] = [fname]

    return duplicate

def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as: ScriptName.py NameOfDirectory")
            print("Please provide valid absolute path")
        else:
            dir_name = sys.argv[1]
            duplicate = find_duplicate(dir_name)
            print(duplicate)
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as: ")
        print("--h : Used to display help")
        print("--u : Used to display usage")

if __name__ == "__main__":
    main()


"""
2. Design automation script which accept directory name and write names of duplicate files from that directory into log file named as Log.txt. 
Log.txt file should be created into current directory. 
Usage : DirectoryDusplicate.py 'Demo' 
Demo is name of directory. 
"""