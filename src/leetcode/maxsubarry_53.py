import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_start = 0
        cur_sum = 0
        best_start = 0
        best_end = 0
        best_sum = -sys.maxsize

        for i, x in enumerate(nums):
            cur_sum += x
            print(cur_sum)
            if cur_sum > best_sum:
                    best_sum = cur_sum
                    best_start = cur_start
                    best_end = i + 1
            if cur_sum < 0:
                cur_sum = 0
                cur_start = i + 1

        return best_sum
            
        
