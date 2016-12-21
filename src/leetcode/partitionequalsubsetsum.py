#https://leetcode.com/problems/partition-equal-subset-sum/

import collections

class Solution(object):

    def canPartition(self, nums):
        self.memo = collections.defaultdict(int)
        self.nums = nums
        return self.solve(0, 0) == 0

    def solve(self, diff, i):
        if self.memo[(diff, i)]:
            return self.memo[(diff, i)]
    
        if i == len(self.nums):
            return diff
    
        self.memo[(diff, i)] = min(abs(self.solve(diff + self.nums[i], i + 1)),
                                   abs(self.solve(diff - self.nums[i], i + 1)))

        return self.memo[(diff, i)]
