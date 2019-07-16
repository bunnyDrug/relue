#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import timeit


x = """
from sympy import prime
from sympy import isprime
remaining = 600851475143
factors = []
index = 2

while remaining != 1:
    if isprime(remaining):
        factors.append(remaining)
        remaining = remaining // remaining
        break
    elif remaining % prime(index) == 0:
        remaining = remaining // prime(index)
        factors.append(prime(index))
    else:
        index += 1
"""
print(timeit.timeit(x),number=100)
# print(factors)