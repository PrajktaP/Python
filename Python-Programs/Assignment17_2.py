import schedule
import time
import datetime

def display():
    print("Date and time:", datetime.datetime.now())

def main():
    schedule.every(1).minute.do(display)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


"""
2. Schedule a task that displays the current date and time every minute using the datetime module. 
"""