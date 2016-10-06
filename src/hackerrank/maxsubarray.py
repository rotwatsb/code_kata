#https://www.hackerrank.com/challenges/maxsubarray
import sys

def max_subarray():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        array = [int(x) for x in input().strip().split()]
        solve(array)
        
def solve(array):
    cur_sum = 0
    best_cont_sum = -sys.maxsize - 1
    best_sum = -sys.maxsize - 1
    for x in array:
        cur_sum += x
        best_cont_sum = max(best_cont_sum, cur_sum)
        cur_sum = max(cur_sum, 0)
        best_sum = max(best_sum + x, best_sum, x)
    print(best_cont_sum, end=" ")
    print(best_sum)
