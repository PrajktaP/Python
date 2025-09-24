import os
import sys
import time
import hashlib

# open file in binary mode
# create hashlib object and call md5 to use md5 algo
# read chunk of the file and keep it in buffer
# if the chunk length is > 0, update hashlib obj with the buffer
# read next chunk and keep it in buffer
# re-enter loop with new buffer
# loop will end when there is nothing left to read from file and buffer size becomes 0
# finally 
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
            directory_watcher(dir_name)
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as: ")
        print("--h : Used to display help")
        print("--u : Used to display usage")

if __name__ == "__main__":
    main()


"""
1. Design automation script which accept directory name and display checksum of all files. 
Usage : DirectoryChecksum.py 'Demo' 
Demo is name of directory. 
"""


"""
Understanding of the logic:
1. Open the File in Binary Mode (`rb`). This is important because checksums should be based on the raw bytes of a file, not on its string interpretation.

2. Create an MD5 Hash Object: 
hobj = hashlib.md5()
Uses Python’s built-in hashlib module to create an **MD5 hashing object**.
This object accumulates the file’s contents as you feed it in blocks.
You’ll need to add 'import hashlib' at the top of your script.

3. Read File in Chunks and Update Hash using the defined 'blocksize'.
'hobj.update(buffer)' feeds the chunk of data into the MD5 hash object.
This continues until the whole file is read.

4. Close the File
Always good practice to close the file after you're done reading it.

5. Return the Checksum
hobj.hexdigest()
Return the final MD5 checksum as a hexadecimal string.
Example: '9e107d9d372bb6826bd81d3542a419d6'
"""