import schedule
import time

def check_email():
    print("Checking email...")
    
def main():
    schedule.every(10).seconds.do(check_email)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


"""
8. Write a script that simulates checking for email updates every 10 seconds. (Use a print statement like 'Checking mail...' instead of real email logic.)
"""