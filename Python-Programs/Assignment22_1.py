import sys
import os
import time
import gmail as g
import schedule
import hashlib
from datetime import datetime

def calculateChecksum(path, blocksize = 1024):
    fobj = open(path, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(blocksize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(blocksize)

    fobj.close()

    return hobj.hexdigest()

def arrange_file_and_folder_to_log():
    now = datetime.now()
    formatted = now.strftime("%Y_%m_%d_%H%M%S")

    if not os.path.exists("Marvellous"):
        os.mkdir("Marvellous")
    
    log_file_path = f"Marvellous/FileDeletionHistory_{formatted}.log"

    return log_file_path

def send_email(log_file_path, receiver, body):
    g.send_email_using_gmail(log_file_path, receiver, body)
    print(f"Generated logs and emailed the log file to {receiver}")

# abs_dirname is the dir name where we'll be 
def delete_duplicates_and_log_info(abs_dirname, receiver):
    border = "-"*100

    log_file_path = arrange_file_and_folder_to_log()
    fobj = open(log_file_path, "w")
    fobj.write(f"{border}\n")
    fobj.write(f"********** {time.ctime()} **********\n")

    grouped_files = {}
    start_time = time.ctime()
    for main_dir, sub_dirs, file_names in os.walk(abs_dirname):
        for fname in file_names:
            fname = os.path.join(main_dir, fname)
            check_sum = calculateChecksum(fname)
            if(check_sum in grouped_files):
                grouped_files[check_sum].append(fname)
            else:
                grouped_files[check_sum] = [fname]

    # only select those where each checksum has > 1 files, which means they have duplicates
    duplicates = list(filter(lambda x : len(x) > 1, grouped_files.values()))

    deleted_count = 0
    count = 0
    total_count = 0
    for group in duplicates:
        for item in group:
            if count > 0:
                deleted_count += 1
                fobj.write(f"{item} \n")
                os.remove(item)
            count += 1
            total_count += 1
        count = 0

    fobj.write(f"********** Total files deleted: {deleted_count} **********\n")
    fobj.write(f"{border}\n")
    fobj.close()

    if deleted_count == 0:
        print("No files deleted")
        return()

    # email the log file if any of the files got deleted
    # Form the email body content
    email_body = (
        f"Details of the process\n\n"
        f"Scanning started at: {start_time}\n"
        f"Total number of files scanned: {total_count}\n"
        f"Total number of duplicate files found: {deleted_count}\n\n"
        f"Please find attached the document listing the deleted duplicate files.\n"
    )
    send_email(log_file_path, receiver, email_body)

# code to accept arguments from file input.txt => input redirection
def main():
    abs_dirname = input()
    interval = int(input())
    receiver = input()

    # create directory if it does not exist
    if not os.path.exists(abs_dirname):
        print("Invalid directory path")
        exit()
    
    flag = os.path.isdir(abs_dirname)
    if(flag == False):
        print(f"Path is valid, but target is not a directory")
        exit()

    schedule.every(interval).minutes.do(delete_duplicates_and_log_info, abs_dirname, receiver)

    while(True):
        schedule.run_pending()
        time.sleep(1)
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as: ")
        print("--h : Used to display help")
        print("--u : Used to display usage")

if __name__ == "__main__":
    main()


# python Assignment22_1.py < input.txt  ----- currently in use
# python Assignment22_1.py python_marvellous/Marvellous-Python-Assignments/Assignment_22/Test 1 prajkta.p@gmail.com

"""
Automation Assignment : 22
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.
Design automation script which performs following task.
Accept Directory name from user and delete all duplicate files from the specified directory by
considering the checksum of files.
Create one Directory named as Marvellous and inside that directory create log file which
maintains all names of duplicate files which are deleted.
Name of that log file should contains the date and time at which that file gets created.
Accept duration in minutes from user and perform task of duplicate file removal after the specific
time interval.
Accept Mail id from user and send the attachment of the log file.
Mail body should contains statistics about the operation of duplicate file removal.
Mail body should contains below things :
Starting time of scanning
Total number of files scanned
Total number of duplicate files found
Consider below command line options for the gives script

DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

- DuplicateFileRemoval.py
Name of python automation script
- E:/Data/Demo
Absolute path of directory which may contains duplicate files
- 50
Time interval of script in minutes
- marvellousinfosystem@gmail.com
Mail ID of the receiver
Note :
For every separate task write separate function.
Write all user defined functions in one user defined module.
Use proper validation techniques.
Provide Help and usage option for script.
Create one Readme file which contains description of our script, details of command line options.
"""


"""
Code for accepting arguments through command line =>

def main():
    args = sys.argv
    print(args)

    if(len(args) == 2):
        if((args[1] == "--h") or (args[1] == "--H")):
            print("Script to delete duplicate files and send the log via email")
        elif((args[1] == "--u") or (args[1] == "--U")):
            print("Use the given script as: 'python Assignment22_1.py python_marvellous/Marvellous-Python-Assignments/Assignment_22/Test 1 prajkta.p@gmail.com'")
    elif(len(args) == 4):
        abs_dirname = args[1]
        interval = int(args[2])
        receiver = args[3]

        # create directory if it does not exist
        if not os.path.exists(abs_dirname):
            print("Invalid directory path")
            exit()
        
        flag = os.path.isdir(abs_dirname)
        if(flag == False):
            print(f"Path is valid, but target is not a directory")
            exit()

        schedule.every(interval).minutes.do(delete_duplicates_and_log_info, abs_dirname)

        while(True):
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as: ")
        print("--h : Used to display help")
        print("--u : Used to display usage")

if __name__ == "__main__":
    main()
"""