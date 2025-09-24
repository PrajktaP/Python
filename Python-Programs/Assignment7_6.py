
def CheckPrime(Num):
    factors = []
    for i in range(Num, 0, -1):
        if((Num % i) == 0):
            factors.append(i)

    if sorted(factors) == [1, Num]:
        return True
    else:
        return False

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    for i in range(size):
        Data.append(int(input()))
    
    print("Entered list: ", Data)

    # -- using filter function
    PrimeData = list(filter(CheckPrime, Data))
    print("Prime list: ", PrimeData)

if __name__ == "__main__":
    main()


"""
Q6. Write a function that accepts a list of integers and returns a list of prime numbers
using filter().
Expected Input:
Enter list: 10 11 12 13 14 15 16 17
Expected Output:
Prime numbers: [11, 13, 17]
"""