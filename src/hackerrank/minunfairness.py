n = int(input().strip())
k = int(input().strip())

ns = [int(input().strip()) for x in range(n)]

ns = sorted(ns)

best = ns[k-1]-ns[0]

for i in range(1, n-k+1):
    best = min(best, ns[k+i-1] - ns[i])

print(best)
    


