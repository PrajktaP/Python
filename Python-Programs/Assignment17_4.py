import schedule
import time

def display():
    print("Namarkar!!!")

def main():
    # Schedule the job every day at 9:00 AM
    schedule.every().day.at("09:00").do(display)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


"""
4. Create a task that runs once every day at 9:00 AM and prints 'Namskar...' 
"""