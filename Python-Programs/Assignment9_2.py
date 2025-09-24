import multiprocessing
import time

def Square():
    print("Thread ID of Square method: ", multiprocessing.get_ident())
    print("Thread Name of Square method: ", multiprocessing.current_thread().name)

    for i in range(1, 6):
        print(i, end=" ")
    print()

def main():
    T1 = multiprocessing.Process(target = Square)
    T2 = multiprocessing.Process(target = Square)
    T3 = multiprocessing.Process(target = Square)

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
2. Write a Python program using multiprocessing. Process to square a list of
numbers using multiple processes.
"""