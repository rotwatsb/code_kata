import functools
import operator

def StairCase(n):
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        print("#" * i)

def sum(_numbers):
    return functools.reduce(operator.add, _numbers, 0)
