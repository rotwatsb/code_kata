class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.memo = {}
        return self.solve('', n, 0)

    def solve(self, prefix, to_op, to_cl):
        if to_op <= 0 and to_cl <= 0:
            return [prefix]

        ls = []
        
        for i in range(to_op, 0, -1):
            s = '(' * i
            for j in range(i + to_cl, 0, -1):
                t = ')' * j
                us = self.solve(s + t, to_op - i, to_cl + i - j)
                ls.extend([prefix + u  for u in us])
        return ls

