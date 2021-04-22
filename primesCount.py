from math import sqrt

def checkDivisors(curNumber, primes):
    isPrime = True
    for p in primes:
        if p > sqrt(curNumber):
            break 
        elif curNumber % p == 0: 
            # Theorem1 : all numbers have a prime factorization
            # if some prime strictly smaller than current number divides
            #, then current number is not prime 
            isPrime = False
            break
            
    return isPrime

def primesCount(n):
    primes = [] #array of primes
    curNumber = 2 # number we need to check
    while len(primes) < n:
        isPrime = True
        if curNumber < 4:
            isPrime = checkDivisors(curNumber, primes)
            if isPrime: primes.append(curNumber)
            curNumber += 1
            if curNumber == 4: curNumber = 6
        else: # theorem2 : all primes  > 3 are of the form 6*k + 1 or 6*k - 1
            isPrime = checkDivisors(curNumber -1, primes)
            if isPrime: primes.append(curNumber - 1)
            isPrime = checkDivisors(curNumber + 1, primes)
            if isPrime: primes.append(curNumber + 1)
            curNumber += 6
    return primes
