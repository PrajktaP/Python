import schedule
import time
import datetime
import os

def write_to_file():
    if os.path.exists("Marvellous.txt"):
        file_obj = open("Marvellous.txt", "a")
    else:
        file_obj = open("Marvellous.txt", "w")

    file_obj.write(f"{datetime.datetime.now()} \n")
    file_obj.close()

def main():
    schedule.every(5).minutes.do(write_to_file)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


"""
5. Schedule a job that runs every 5 minutes to write the current time to a file Marvellous.txt. 
"""