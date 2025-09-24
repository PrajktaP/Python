import psutil

def process_scan():
    process_list = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid', 'name', 'username'])
            process_list.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        
    return process_list

def main():
    arr = process_scan()

    for value in arr:
        print(value)

if __name__ == "__main__":
    main()



"""
1.Design automation script which display information of running processes as its name, PID,
Username.
Usage : ProcInfo.py
"""
