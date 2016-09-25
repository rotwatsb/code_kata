#https://projecteuler.net/problem=12
import math
from sympy.ntheory import factorint

def solve():
    i = 2
    tri_num = 1
    while num_factors(tri_num) < 500:
        i += 1
        tri_num += i
    print("{} has +500 factors".format(tri_num))

def num_factors(n):
    prime_fact = factorint(n)
    factors = 1
    for k in prime_fact.keys():
        factors *= prime_fact[k]+1
    return factors
