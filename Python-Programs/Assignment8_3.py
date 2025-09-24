import threading

def EvenList(ListOfNumbers):
    SumEvenList = 0
    even_list = []

    for i in ListOfNumbers:
        if i % 2 == 0:
            even_list.append(i)
            SumEvenList = SumEvenList + i

    print(f"Sum of even numbers {even_list} is: ", SumEvenList)

def OddList(ListOfNumbers):
    SumOddList = 0
    odd_list = []

    for i in ListOfNumbers:
        if i % 2 != 0:
            odd_list.append(i)
            SumOddList = SumOddList + i

    print(f"Sum of odd numbers {odd_list} is: ", SumOddList)

def main():
    try:
        size = int(input("Enter number of elements: "))

        ListOfNumbers = []
        for i in range(size):
            ListOfNumbers.append(int(input("Enter a number: ")))

        T1 = threading.Thread(target = EvenList, args=(ListOfNumbers, ))
        T2 = threading.Thread(target = OddList, args=(ListOfNumbers, ))

        T1.start()
        T2.start()

        T1.join()
        T2.join()

    except ValueError as vobj:
        print("Invalid Value entered:", vobj)
    except TypeError as tobj:
        print("Invalid Type:", tobj)
    except Exception as eobj:
        print("Exception occurred:", eobj)

    print("Exit from main")

if __name__ == "__main__":
    main()


"""
3.Design python application which creates two threads as evenlist and oddlist. Both the
threads accept list of integers as parameter. Evenlist thread add all even elements
from input list and display the addition. Oddlist thread add all odd elements from input
list and display the addition.
"""