import schedule
import time
import datetime
import os

def log_details(current_timestamp, status):
    
    if os.path.exists("backup_log.txt"):
        file_obj = open("backup_log.txt", "a")
    else:
        file_obj = open("backup_log.txt", "w")

    if(status == 1):
        file_obj.write(f"Backup done successfully at: {current_timestamp}\n")
    else:
        file_obj.write(f"Backup failed at: {current_timestamp}\n")
    
    file_obj.close()

def take_backup():
    current_timestamp = datetime.datetime.now()
    try:
        datetime_string = current_timestamp.strftime('%a%d%b%Y%I%M%S')
        file_obj = open(f"file_{datetime_string}", "w")
        file_obj.write(f"{current_timestamp}\n")
        file_obj.close()

        log_details(current_timestamp, 1)
    except Exception as eobj:
        log_details(current_timestamp, 0)

def main():
    schedule.every().hour.do(take_backup)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


"""
7. Schedule a function that performs file backup every hour and writes a log entry into backup_log.txt. 
"""