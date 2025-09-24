import schedule
import time
import datetime

def notify_lunch_time():
    print("Lunch time!!")

def notify_wrap_up_work():
    print("Wrap up work!!")

def main():
    schedule.every().day.at("13:00").do(notify_lunch_time)
    schedule.every().day.at("18:00").do(notify_wrap_up_work)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


"""
6. Write a script that schedules multiple tasks: one to print 'Lunch Time!' at 1 PM, and another to print 'Wrap up work' at 6 PM. 
"""