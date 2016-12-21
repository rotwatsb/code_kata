def lis():
    n = int(input().strip())
    nums = [int(input().strip()) for _ in range(n)]
    solve2(nums)

def solve(nums):
    l = len(nums)
    memo = [1] * l
    best = 1
    for i in range(l):
        for j in range(0, i):
            if nums[j] < nums[i]:
                memo[i] = max(memo[j] + 1, memo[i])
        best = max(best, memo[i])
    print(best)

def find_small(nums, x):
    i = 0
    j = len(nums) - 1
    while i != j:
        mid = (i + j) // 2 if j - i > 1 else i
        if nums[mid] < x:
            i = mid if j - i > 1 else j
        elif nums[mid] == x:
            return mid
        else:
            j = mid
    while nums[i] < x:
        i += 1
    return i
    

def solve2(nums):
    l = len(nums)
    ends = []

    for n in nums:
        if ends:
            if n > ends[len(ends) - 1]:
                ends.append(n)
            else:
                i = find_small(ends, n)
                ends[i] = n
        else:
            ends.append(n)
    print(len(ends))
