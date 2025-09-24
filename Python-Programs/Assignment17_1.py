import schedule
import time

def display():
    print("Jay Ganesh..")

def main():
    schedule.every(2).seconds.do(display)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


"""
1. Write a Python script that prints 'Jay Ganesh...' every 2 seconds. Use the schedule.every(2).seconds.do(...) function. 
"""