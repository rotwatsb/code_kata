class Solution(object):
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        memo = [[None] * n for _ in range(n)]
        x = self.solve(nums, n-1, n-1, memo, False)
        x.reverse()
        return x
        
    def solve(self, nums, i, j, memo, taken):
        if i == 0:
            return [nums[i]] if not taken or (nums[j] % nums[i] == 0 and taken) else []
        elif memo[i][j] and taken:
            return memo[i][j]

        if not taken or (nums[j] % nums[i] == 0 and taken):
            l1 = [nums[i]]
            l1.extend(self.solve(nums, i-1, i, memo, True))
            l2 = self.solve(nums, i-1, j, memo, taken)
            memo[i][j] = l1 if len(l1) > len(l2) else l2
        else:
            memo[i][j] = self.solve(nums, i-1, j, memo, taken)
        return memo[i][j]

'''        
        sets = [set()]
        for n in nums:
            to_add = []
            for s in sets:
                x = set(s)
                x.add(n)
                to_add.append(x)
            sets.extend(to_add)
        ok_sets = []
        for s in sets:
            ok_sets.append(s)
            self.set_ok(s, ok_sets)
            
        print(ok_sets)

    def set_ok(self, s, ok_sets):
        for a in s:
            for b in s:
                if not a == b:
                    if not (a % b == 0 or b % a == 0):
                        ok_sets.pop()
                        return
                        
'''
