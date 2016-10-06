#https://www.hackerrank.com/challenges/coin-change?h_r=next-challenge&h_v=zen

def coin_change():
    n_and_m = [int(x) for x in input().strip().split()]
    n = n_and_m[0]
    coins = [int(x) for x in input().strip().split()]
    coins.sort()
    #print(solve(n, coins))
    print(solve2([n], [0], coins))

def solve(val, coins):
    combinations = 0
    for i, coin in enumerate(coins):
        if coin < val:
            combinations += solve(val - coin, coins[i:])
        elif coin == val:
            combinations += 1
        elif coin > val:
            break
    return combinations

def solve2(val_stack, i_stack, coins):
    while val_stack:
        val = val_stack.pop()
        i = i_stack.pop()
        combinations = 0
        while i < len(coins):
            if coin[i] < val:
                val_stack.append(val - coin)
                i_stack.append(i)
            elif coin[i] == val:
                combinations += 1
            elif coin[i] > val:
                break
            
    
    
