#https://leetcode.com/problems/combination-sum-iv/
class Solution(object):
    def combinationSum4(self, nums, target):
        memo = {}
        return self.combsum(nums, target, memo)

    def combsum(self, nums, target, memo):
        if target in memo:
            return memo[target]
        count = 0
        for num in nums:
            if num < target:
                count += self.combsum(nums, target - num, memo)
            elif num == target:
                count += 1
        memo[target] = count
        return count
