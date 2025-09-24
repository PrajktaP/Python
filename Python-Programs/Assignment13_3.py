class Arithmetic:
    def __init__(self, value):
        self.value = value

    def check_prime(self):
        facts = []
        for num in range(1, self.value+1):
            if self.value % num == 0:
                facts.append(num)

        if sorted(facts) == [1, num]:
            return True
        else:
            return False

    def check_perfect(self):
        sum = 0
        for num in range(1, self.value):
            if self.value % num == 0:
                sum += num
        
        if sum == self.value:
            return True
        else:
            return False

    def sum_factors(self):
        sum = 0
        for num in range(1, self.value+1):
            if self.value % num == 0:
                sum += num

        return sum

    def factors(self):
        facts = []
        for num in range(1, self.value+1):
            if self.value % num == 0:
                facts.append(num)

        return facts


def main():
    try: 
        num = int(input("Enter a number: "))

        obj = Arithmetic(num)

        prime = obj.check_prime()
        if prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")

        perfect = obj.check_perfect()
        if perfect:
            print(f"{num} is a perfect number.")
        else:
            print(f"{num} is not a perfect number.")

        facts = obj.factors()
        print("Factors are: ", facts)

        sum_of_facts = obj.sum_factors()
        print("Sum of the factors are: ", sum_of_facts)

        
    except ValueError as vobj:
        print("Invalid value entered: ", vobj)
    except Exception as eobj:
        print("Exception occurred: ", eobj)

if __name__ == "__main__":
    main()

"""
3. Write a program which contains one class named as Numbers.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There
are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required.
After designing the above class call all instance methods by creating multiple objects.
"""

"""
A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
For example:
The number 28 is a perfect number because:
Its divisors (excluding 28) are: 1, 2, 4, 7, 14
If you add them up: 1 + 2 + 4 + 7 + 14 = 28
"""