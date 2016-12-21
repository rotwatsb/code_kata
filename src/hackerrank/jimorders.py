n = int(input().strip())

tds = []
for i in range(n):
    t, d = input().strip().split(' ')
    tds.append((int(t) + int(d), i))

tds.sort()
for td in tds:
    print(td[1] + 1, end=" ")

