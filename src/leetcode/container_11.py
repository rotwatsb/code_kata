class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0;
        j = len(height) - 1;
        best = 0;
        while i < j:
            best = max(best, min(height[i], height[j]) * (j - i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return best
        
"""
        self.memo = [-1] * len(height)
        return self.solve(len(height) - 1, len(height) - 1, height) if height else 0

    def solve(self, i, right, h):
        if self.memo[i] > -1:
            return self.memo[i]
        
        v = min(h[i], h[right]) * (right - i)

        self.memo[i] = max(v, self.solve(i - 1, right, h), self.solve(i-1, i, h)) if i > 0 else v
        return self.memo[i]
"""
