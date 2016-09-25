# https://github.com/recursecenter/interview-prep/blob/master/_questions/taxi-driver.md

def taxi_driver():
    n = int(input())
    mem = [[helper(i, j) for i in range(n)] for j in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            mem[i][j] = mem[i-1][j] + mem[i][j-1]
    return mem[n-1][n-1]

def helper(i, j):
    if (i == 0 or j == 0):
        return 1
    else:
        return 0

print(taxi_driver())

