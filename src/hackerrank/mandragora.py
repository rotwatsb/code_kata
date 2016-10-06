#https://www.hackerrank.com/challenges/mandragora

def mandragora():
    t = int(input().strip())
    for _ in range(t):
        n = input()
        healths = [int(x) for x in input().strip().split()]
        healths.sort()
        solve(healths)

def solve(healths):
    cur_sum = 0
    sums = []
    #want a sums where sums[i] = sum of all array[j], j >= i
    for x in reversed(healths):
        sums.append(cur_sum)
        cur_sum += x
    sums.reverse()

    s = 1
    p = 0

    for i, h in enumerate(healths):
        if s * healths[i] > sums[i]:
            p += s * h
        else:
            s += 1
            

    print(p)
