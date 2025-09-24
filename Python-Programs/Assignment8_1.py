import threading

def DisplayEven():
    x = 1
    y = 0
    Data = []
    while y < 10:
        if x % 2 == 0:
            Data.append(x)
            y = y + 1
        x = x + 1
    print(Data)

def DisplayOdd():
    x = 1
    y = 0
    Data = []
    while y < 10:
        if x % 2 != 0:
            Data.append(x)
            y = y + 1
        x = x + 1
    print(Data)
        
def main():
    try:
        T1 = threading.Thread(target = DisplayEven)
        T2 = threading.Thread(target = DisplayOdd)
        T1.start()
        T2.start()
        T1.join()
        T2.join()
    except Exception as eobj:
        print("Exception occurred:", eobj)

if __name__ == "__main__":
    main()


"""
1.Design python application which creates two thread named as even and odd. Even
thread will display first 10 even numbers and odd thread will display first 10 odd
numbers.
"""