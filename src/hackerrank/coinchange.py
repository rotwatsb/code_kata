#https://www.hackerrank.com/challenges/coin-change?h_r=next-challenge&h_v=zen

def coin_change():
    n_and_m = [int(x) for x in input().strip().split()]
    n = n_and_m[0]
    coins = [int(x) for x in input().strip().split()]
    coins.sort()
    
    #print(solve(n, coins))
    print(solve2(n, coins))
    
    
def solve(val, coins):
    combinations = 0
    for i, coin in enumerate(coins):
        if coin < val and val - coin >= coin:
            combinations += solve(val - coin, coins[i:])
        elif coin == val:
            combinations += 1
        elif coin > val:
            break
    return combinations

def solve2(val, coins):
    m = len(coins)
    n = val
    memo = [[0 for _ in range(m)] for _ in range(n+1)]
    for i in range(m):
        memo[0][i] = 1

    for i in range(1, n+1):
        for j in range(m):
            x = memo[i - coins[j]][j] if i - coins[j] >= 0 else 0
            y = memo[i][j-1] if j > 0 else 0
            memo[i][j] = x + y
    return memo[val][m-1]
    
    
