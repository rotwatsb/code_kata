class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates = sorted(candidates)
        
        return self.solve(candidates, target)
    
    def solve(self, candidates, target):
        sl = []
        for i, c in enumerate(candidates):
            if c < target:
                s = self.solve(candidates[i:], target - c)
                for x in s:
                    x.append(c)
                    sl.append(x)
            elif c == target:
                sl.append([c])
            else:
                return sl
        return sl
            
                                

        
        
        
