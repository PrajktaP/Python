import threading

# char.islower()
# char.isupper()
# char.isdigit()

def DisplaySmall(InputString):
    print("Thread ID of DisplaySmall method: ", threading.get_ident())
    print("Thread Name of DisplaySmall method: ", threading.current_thread().name)
    count = 0

    for i in InputString:
        if i.islower():
            count = count + 1
            
    print(f"Total count of Small letters: ", count)

def DisplayCapital(InputString):
    print("Thread ID of DisplayCapital method: ", threading.get_ident())
    print("Thread Name of DisplayCapital method: ", threading.current_thread().name)
    count = 0

    for i in InputString:
        if i.isupper():
            count = count + 1
            
    print(f"Total count of Capital letters: ", count)

def DisplayDigits(InputString):
    print("Thread ID of DisplayDigits method: ", threading.get_ident())
    print("Thread Name of DisplayDigits method: ", threading.current_thread().name)
    count = 0

    for i in InputString:
        if i.isdigit():
            count = count + 1
            
    print(f"Total count of Digits: ", count)

def main():
    try:
        StringInput = input("Enter a string: ")
        print() # added this just to see clean output

        T1 = threading.Thread(target = DisplaySmall, args=(StringInput, ))
        T2 = threading.Thread(target = DisplayCapital, args=(StringInput, ))
        T3 = threading.Thread(target = DisplayDigits, args=(StringInput, ))

        T1.start()
        T2.start()
        T3.start()

        T1.join()
        T2.join()
        T3.join()

    except ValueError as vobj:
        print("Invalid Value entered:", vobj)
    except TypeError as tobj:
        print("Invalid Type:", tobj)
    except Exception as eobj:
        print("Exception occurred:", eobj)

    print("\nExit from main")

if __name__ == "__main__":
    main()


"""
4.Design python application which creates three threads as small, capital, digits. 
All the threads accepts string as parameter. 
Small thread display number of small characters, capital thread display number of capital characters and digits thread display number of digits. 
Display id and name of each thread.
"""