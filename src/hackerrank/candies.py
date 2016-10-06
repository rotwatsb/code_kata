#https://www.hackerrank.com/challenges/candies
import sys

def candies():
    n = int(input())
    ranks = []
    for i in range(n):
        ranks.append(int(input()))

    candies = [1] * n

    candy_amt = 1
    last_rank = ranks[0]
    for i in range(1, n):
        if ranks[i] > last_rank:
            candy_amt += 1
            candies[i] = max(candies[i], candy_amt)
        else:
            candy_amt = 1
        last_rank = ranks[i]
        
    candy_amt = 1
    last_rank = ranks[n-1]
    for i in range(n - 2, -1, -1):
        if ranks[i] > last_rank:
            candy_amt += 1
            candies[i] = max(candies[i], candy_amt)
        else:
            candy_amt = 1
        last_rank = ranks[i]

    print(sum(candies))

candies()
        
