class Solution(object):
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)
        memo = [[0 for y in nums] for x in nums]
        self.wiggle_max(len(nums) - 1, len(nums) - 1, nums, memo, 0, False)
        return memo[len(nums) - 1][len(nums) - 1]

    def wiggle_max(self, i, j, nums, memo, num_taken, last_diff):
        if memo[i][j]:
            return memo[i][j]
        
        count = 0
        if num_taken >= 2:
            if ((nums[i] - nums[j] < 0 and last_diff > 0) or
                (nums[i] - nums[j] > 0 and last_diff < 0)):
                if i == 0:
                    count = 1
                else:
                    count = max(1 + self.wiggle_max(i - 1, i, nums, memo, num_taken+1, nums[i] - nums[j]),
                                self.wiggle_max(i - 1, j, nums, memo, num_taken, last_diff))
            else:
                if not i == 0:
                    count = self.wiggle_max(i - 1, j, nums, memo, num_taken, last_diff)
        else:
            if i == 0:
                if num_taken == 1 and not nums[i] == nums[j]:
                    count = 1
                elif num_taken == 0:
                    count = 1
            else:
                if num_taken == 0 or (num_taken == 1 and not nums[i] == nums[j]):
                    count = max(1 + self.wiggle_max(i - 1, i, nums, memo, num_taken+1, nums[i] - nums[j]),
                                self.wiggle_max(i - 1, j, nums, memo, num_taken, last_diff))
            
        memo[i][j] = count
        return count
'''
