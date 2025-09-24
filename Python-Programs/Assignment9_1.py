import threading
import time

def Display():
    print("Thread ID of Display method: ", threading.get_ident())
    print("Thread Name of Display method: ", threading.current_thread().name)

    for i in range(1, 6):
        print(i, end=" ")
    print()

def main():
    T1 = threading.Thread(target = Display)
    T2 = threading.Thread(target = Display)
    T3 = threading.Thread(target = Display)

    T1.start()
    time.sleep(1)
    T2.start()
    time.sleep(1)
    T3.start()
    time.sleep(1)

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()



"""
1.Create a Python program that starts 3 threads, each printing numbers
from 1 to 5 with a delay of 1 second. Use threading.Thread.
"""