import psutil
import os
import sys

def log_running_processes(filepath):
    if os.path.exists(filepath):
        fobj = open(filepath, "a")
    else:
        fobj = open(filepath, "w")

    # add border in log file
    border = "*"*100
    fobj.write(f"{border} \n Process Logs \n{border} \n")

    # iterate through all the running processes
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid', 'name', 'username'])
        fobj.write(f"{info}\n")

    fobj.close

def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("Design automation script which accept directory name from user and create log file in that directory which contains information of running processes as its name, PID, Username.")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as: ScriptName.py NameOfDirectory")
        else:
            dirname = sys.argv[1]

            # create directory if it does not exist
            if not os.path.exists(dirname):
                os.mkdir(dirname)

            # get log file's path
            path = os.path.join(dirname, 'process_logs.log')

            log_running_processes(path)

if __name__ == "__main__":
    main()



"""
3. Design automation script which accept directory name from user and create log file in that
directory which contains information of running processes as its name, PID, Username.
Usage : ProcInfoLog.py Demo
Demo is name of Directory.
"""

# python Assignment21_3.py Demo