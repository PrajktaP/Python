import threading
import multiprocessing
import time

def SumOfNumbers(origin):
    sum = 0
    for i in range(1, 10000001):
        sum += i

    print(f"Sum of numbers from 1 to 10 million using {origin}: ", sum)

def main():
    start = time.time()
    SumOfNumbers("normal function")
    end = time.time()
    print("Time taken for normal function call: ", end - start)
    print()

    start = time.time()
    T = threading.Thread(target = SumOfNumbers, args=("threading", ))
    T.start()
    T.join()
    end = time.time()
    print("Time taken with threading: ", end - start)
    print()

    start = time.time()
    P = multiprocessing.Process(target = SumOfNumbers, args=("multiprocessing", ))
    P.start()
    P.join()
    end = time.time()
    print("Time taken with multiprocessing: ", end - start)
    print()

    print("Exiting main")


if __name__ == "__main__":
    main()


"""
4. Create a Python program that Compare execution time of summing
numbers from 1 to 10 million using normal function, threading, and
multiprocessing.
"""