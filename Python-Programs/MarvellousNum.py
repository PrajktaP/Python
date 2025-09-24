def ChkPrime(num):
    factors = []

    for i in range(num, 0, -1):
        if((num % i) == 0):
            factors.append(i)

    if sorted(factors) == [1, num]:
        return True
    else:
        return False