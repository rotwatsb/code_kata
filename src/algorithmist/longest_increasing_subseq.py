def solve(seq):
    l = len(seq)
    memo = [[None for x in range(l)] if y != 0 else [1 if seq[0] < x else 0 for x in seq] for y in range(l)]
    n = longest(seq, memo, l-1, l-1, False)
    print_matrix(memo)
    return n

def longest(seq, memo, r, c, taken_elem):
    if memo[r][c] is not None:
        return memo[r][c]
    else:
        if seq[r] >= seq[c] and taken_elem:
            memo[r][c] = longest(seq, memo, r-1, c, taken_elem)
        else:
            memo[r][c] = max(1 + longest(seq, memo, r-1, r, True),
                             longest(seq, memo, r-1, c if taken_elem else r-1, taken_elem))
    return memo[r][c]

def print_matrix(m):
    for l in reversed(m):
        print(l)
