class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.memo = {}
        
        if not s:
            return 0

        x = self.solve(s)
        return x

    def solve(self, s):
        if s in self.memo:
            return self.memo[s]

        for i, c in enumerate(s):
            if c == '0':
                return 0
            if i < len(s) - 1:
                if c == '1' or c == '2':
                    if s[i+1] == '0':
                        self.memo[s] = self.solve(s[i + 2:])
                        return self.memo[s]
                    elif ((s[i+1] >= '1' and s[i+1] <= '6') or c == '1'):
                        self.memo[s] = self.solve(s[i + 1:]) + self.solve(s[i + 2:])
                        return self.memo[s]
                    
        return 1
