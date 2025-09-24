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
    if(os.path.exists("Log.txt")):
        mode = "a"
    else:
        mode = "w"
    fobj = open("Log.txt", mode)

    fobj.write(f"{time.ctime()} Deleted file {file_name} \n")

def delete_duplicate(dir_name = 'Marvellous'):
    duplicate_dict = find_duplicate(dir_name)

    result = list(filter(lambda x : len(x) > 1, duplicate_dict.values()))
    
    count = 0
    deleted_count = 0
    for values in result:
        for sub_value in values:
            count += 1
            if count > 1:
                deleted_count += 1
                log_duplicate(sub_value)
                os.remove(sub_value)
        count = 0
    print("Total deleted files: ", deleted_count)

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
            delete_duplicate(dir_name)
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as: ")
        print("--h : Used to display help")
        print("--u : Used to display usage")

if __name__ == "__main__":
    main()


"""
3. Design automation script which accept directory name and delete all duplicate files from that directory. 
Write names of duplicate files from that directory into log file named as Log.txt. 
Log. txt file should be created into current directory. 
Usage : DirectoryDusplicateRemoval.py 'Demo' 
Demo is name of directory. 
"""