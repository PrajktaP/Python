import schedule
import time

def remind():
    print("Do coding..!")

def main():
    schedule.every(30).minutes.do(remind)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


"""
3. Write a program that schedules a function to print 'Do Coding..!' every 30 minutes. 
"""