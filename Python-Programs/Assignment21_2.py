import sys
import psutil

def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("Design automation script which accept process name and display information of that process if it is running.")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as: ScriptName.py Notepad")
        else:
            process_name = sys.argv[1]

            for proc in psutil.process_iter():
                info = proc.as_dict(attrs=['pid', 'name', 'username'])
                if info['name'] == process_name:
                    print(f"{process_name} is running: ")
                    print(f"PID is {info['pid']}")
                    print(f"Username is {info['username']}")

if __name__ == "__main__":
    main()



"""
2.Design automation script which accept process name and display information of that process if it is running.
Usage : ProcInfo.py Notepad
"""
