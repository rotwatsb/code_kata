class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        highest = 0
        hi = 0
        
        for i, h in enumerate(height):
            if h > highest:
                highest = h
                hi = i

        total = 0
        prev = 0
        for h in height[0:hi]:
            if h < prev:
                total += prev - h
            elif h > prev:
                prev = h

        prev = 0
        for i in range(len(height) - 1, hi, -1):
            h = height[i]
            if h < prev:
                total += prev - h
            elif h > prev:
                prev = h

        return total
                
