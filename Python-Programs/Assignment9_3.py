import os
import multiprocessing

def Factorial(no):
    print("PID is: ", os.getpid())
    fact = 1
    for i in range(1, no + 1):
        fact = fact * i

    return fact

def main():
    Data = [10, 20, 25, 30, 15, 50, 40, 5, 25]

    result = []
    
    pool = multiprocessing.Pool()
    result = pool.map(Factorial, Data)

    pool.close()
    pool.join()

    print(result)

if __name__ == "__main__":
    main()

"""
3. Create a Python program that uses multiprocessing.Pool to compute
factorial of numbers in a list.
"""