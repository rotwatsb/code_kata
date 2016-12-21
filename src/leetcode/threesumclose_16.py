import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        prev = None
        best_sum = sys.maxsize
        for i, n in enumerate(nums):
            if n == prev or i >= len(nums) - 2:
                continue
            amt = self.twosumclosest(nums[i + 1:], target - n)
            if abs(amt + n - target) < abs(best_sum - target):
                best_sum = amt + n
            prev = n
    
        return best_sum 

    
    def twosumclosest(self, nums, target):
        a = None
        b = None
        for i, n in enumerate(nums):
            c = self.closest(nums[:i], target - n, sys.maxsize)
            if (not a and not a == 0) or abs((c + n) - target) < abs((a + b) - target):
                a = c
                b = n

        return a + b

    def closest(self, l, x, best):
        if not l:
            return best
        i = len(l) // 2
        if l[i] == x:
            return l[i]

        best = best if abs(best - x) < abs(l[i] - x) else l[i]
        if x < l[i]:
            return self.closest(l[:i], x, best)
        else:
            return self.closest(l[i + 1:], x, best)


class TreeNode(object):
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return "{}({}, {})".format(self.val, str(self.left), str(self.right))

    def closest(self, x, best):
        if not self.val and not self.val == 0:
            return sys.maxsize
        
        if x == self.val:
            return self.val

        best = best if abs(best - x) < abs(self.val - x) else self.val
        
        if x < self.val and self.left:
            return self.left.closest(x, best)
        elif self.right:
            return self.right.closest(x, best)

        return best

    def add(self, x):
        if not self.val and not self.val == 0:
            self.val = x
        elif x <= self.val:
            if self.left:
                self.left.add(x)
            else:
                self.left = TreeNode(x)
        else:
            if self.right:
                self.right.add(x)
            else:
                self.right = TreeNode(x)

    

        
