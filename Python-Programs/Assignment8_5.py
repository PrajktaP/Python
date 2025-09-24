import threading

def DisplayAscOrder():
    for i in range(1, 51):
        print(i, end=" ")
    print()

def DisplayDescOrder():
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()

def main():
    try:
        thread1 = threading.Thread(target = DisplayAscOrder)
        thread2 = threading.Thread(target = DisplayDescOrder)
        
        thread1.start()
        thread1.join()

        thread2.start()
        thread2.join()

    except TypeError as tobj:
        print("Invalid Type:", tobj)
    except Exception as eobj:
        print("Exception occurred:", eobj)

    print("Exit from main")

if __name__ == "__main__":
    main()


"""
5.Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
screen. After execution of thread1 gets completed then schedule thread2.
"""