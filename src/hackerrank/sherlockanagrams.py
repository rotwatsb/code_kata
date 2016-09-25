import collections

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

def count_nested(s, i, j):
    if j < i:
        return 0
    elif s[i] == s[j]:
        return 1 + count_nested(s, i + 1, j - 1)
    else:
        return 0

def solve_sa(s):
    freqs = collections.defaultdict(int)
    for i in range(len(s)):
        for j in range(i, len(s)):
            freqs[''.join(sorted(s[i:j+1]))] += 1
    print(sum(v * (v-1) // 2 for v in freqs.values()))
'''
def solve_sa_old(s):
    cpos = collections.defaultdict(list)
    for i, c in enumerate(s):
        cpos[c].append(i)
    count = 0
    for c in list(cpos.keys()):
        bonus = 0
        last_pos = -1
        for pos in cpos[c]:
            if last_pos >= 0:
                if pos - last_pos == 1:
                    bonus -= 1
                else:
                    bonus += count_nested(s, last_pos + 1, pos - 1) if last_pos + 1 < pos - 1 else 0
            last_pos = pos
        count += (sum_n(len(cpos[c]) - 1) * 2 + bonus)
    print(count)
'''
n = int(input())
for i in range(n):
    x = input()
    solve_sa(x)


