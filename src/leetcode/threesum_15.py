class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        prev = None
        ls = []
        for i, n in enumerate(nums):
            if n == prev:
                continue
            ls.extend(self.twosum(nums[i + 1:], -n))
            prev = n

        return ls

    def twosum(self, nums, target):
        seen = {}
        ls = []
        prev = None
        for n in nums:
            if n in seen and len(seen[n]) < 3 and not n == prev:
                seen[n].append(n)
                ls.append(seen[n])
                prev = n
            else:
                seen[target - n] = [-target, n]
        return ls
