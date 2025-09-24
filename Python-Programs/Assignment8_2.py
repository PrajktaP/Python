import threading

def EvenFactors(num):
    SumEvenFacts = 0
    EvenFacts = []

    for i in range(1, num + 1):
        if i % 2 == 0 and num % i == 0:
            EvenFacts.append(i)
            SumEvenFacts = SumEvenFacts + i

    print(f"Sum of even factors {EvenFacts} is: ", SumEvenFacts)

def OddFactors(num):
    SumOddFacts = 0
    OddFacts = []

    for i in range(1, num + 1):
        if i % 2 != 0 and num % i == 0:
            OddFacts.append(i)
            SumOddFacts = SumOddFacts + i

    print(f"Sum of odd factors {OddFacts} is: ", SumOddFacts)

def main():
    try:
        num = int(input("Enter a number: "))

        T1 = threading.Thread(target = EvenFactors, args=(num,))
        T2 = threading.Thread(target = OddFactors, args=(num,))

        T1.start()
        T2.start()

        T1.join()
        T2.join()

    except ValueError as vobj:
        print("Invalid Value entered:", vobj)
    except Exception as eobj:
        print("Exception occurred:", eobj)

    print("Exit from main")

if __name__ == "__main__":
    main()


"""
2.Design python application which creates two threads as evenfactor and oddfactor.
Both the thread accept one parameter as integer. Evenfactor thread will display
addition of even factors of given number and oddfactor will display addition of odd
factors of given number. After execution of both the thread gets completed main
thread should display message as “exit from main”.
"""