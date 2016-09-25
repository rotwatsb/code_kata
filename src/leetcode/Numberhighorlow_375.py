import sys
import pdb
import time

class Solution(object):
    def getMoneyAmount1(self, n):
        start_time = time.time()
        memo = [[0] * (n+1) for _ in range(n+1)]
        x = self.minimax1(1, n, memo)
        print("--- {} seconds ---".format(time.time() - start_time))
        return x


    def getMoneyAmount2(self, n):
        start_time = time.time()
        memo = [[0] * (n+1) for _ in range(n+1)]
        x = self.minimax2(1, n, sys.maxsize, 0, 0, True, memo)
        print("--- {} seconds ---".format(time.time() - start_time))
        return x

    def minimax1(self, lowest, highest, memo):
        if lowest >= highest:
            return 0
        if memo[lowest][highest]:
            return memo[lowest][highest]
        memo[lowest][highest] = min(i + max(self.minimax1(lowest, i-1, memo), self.minimax1(i+1, highest, memo)) for i in range(lowest, highest+1))
        return memo[lowest][highest]
    
    def minimax2(self, lowest, highest, a, b, guess, minimize, memo):
        if lowest > highest:
            return -guess
        elif lowest == highest:
            return 0
        
        if minimize:
            if memo[lowest][highest]:
                return memo[lowest][highest]
            
            best = sys.maxsize
            for i in range(lowest, highest + 1):
                v = self.minimax2(lowest, highest, a, b, i, False, memo)
                best = min(best, v)
                a = min(a, v)
                if b > a:
                    break
                
            memo[lowest][highest] = best
            return best
        else:
            v1 = guess + self.minimax2(lowest, guess - 1, a, b, guess, True, memo)
            b = max(b, v1)
            if b > a:
                return v1
            v2 = guess + self.minimax2(guess + 1, highest, a, b, guess, True, memo)
            return max(v1, v2)

