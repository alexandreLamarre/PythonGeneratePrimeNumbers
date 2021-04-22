# PythonGeneratePrimeNumbers
Solution for generating the first 'n' primes.

To check a number is prime, we need to check all its divisors. However, we can make use of certain heuristics to eliminate
many of the divisors:
- We can exclude any divisor less than sqrt(curNumber) since multiplication is associative `a*b = b*a` and `sqrt(n)^2 = n` => there will be no factors `> sqrt(n)` in its divisor decomposition.
- We can exlude any non prime divisor, since every number has a prime number factorization. (we can reuse the list of current primes for this purpose)

Therefore if a number has no prime divisors `<=sqrt(curNumber)` then it must be prime itself.

Now in a simple solution we would check each number starting with 2 if it is prime. To speed up this process, there is a handy theorem in Number theory which states
that all primes (greater than 3) have a remainder of 1 or -1 when divided by 6. You can find an overview of the proof [here](https://math.stackexchange.com/a/150984).
This speeds up the process of checking every number since we can instead increment `curNumber` by 6 after 3 and check the numbers `curNumber - 1` and `curNumber + 1`. We end up checking only 2 numbers every 6 resulting in algorithm that is **3x faster**

### Benchmarks
| Input | Performance |
| :---: | :---------: |
| 10000 | ~`180ms` |
| 100000 | ~`2600ms` |

## Runtime Complexity

The primes follow the following distribution (as an upper bound) `x / ln(x)` where x is the number of primes we are searching for. 
So we search an inversely proportional number of numbers before reaching our desired amount of prime numbers.
Therefore the runtime Complexity is ~`O(2^n)` just for searching the appropriate amount of numbers.
Checking the prime divisors at every number is `1 + 2 + .... + n` since we want n primes. 
This sequence is bounded above by `O(n^2)` so our final worst case (which is not a tight bound - since a tight bound on the number of primes is an open question in mathematics) is approximately **O(n^2 * 2^n)**.

We only use O(n) additional space for the list of primes we are returning.

## Code
```
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

def primes_count(n):
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
```

