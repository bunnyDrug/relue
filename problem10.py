#Problem 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

from sympy import prime
from itertools import count
import math

problem_number = 2000000

primes = []
for i in count(start=1, step=1):
    p = prime(i)
    if p < problem_number:
        primes.append(p)
    else:
        break

print(sum(primes))
