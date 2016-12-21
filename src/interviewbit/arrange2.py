def solve(horses, k):

    memo = [[0 for _ in horses] for _ in range(k)]

    for i in range(k):
        w = 0
        b = 0
        for j in range(len(horses) - 1, -1, -1):
            if horses[j] == 'w':
                w += 1
            else:
                b += 1
                
            if i == 0:
                memo[i][j] = w * b
            else:
                wh = 0
                bh = 0
                best = memo[i-1][j]
                for l in range (j, len(horses) - 1):
                    if horses[l] == 'w':
                        wh += 1
                    else:
                        bh += 1
                    best = min(best, wh * bh + memo[i-1][l+1])
                memo[i][j] = best
    print(memo[k-1][0])

wwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwbwwwwwbwbwbwbwbwbwbwbwbbbwbwbwbwbwbwbwb
