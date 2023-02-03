class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0

        truths = [True] * n

        truths[0], truths[1] = False, False

        i = 0
        while i*i <= n: # 
            if truths[i]: 
                for j in range(i+i,n,i):
                    truths[j] = False
            i += 1
            
        return sum(truths)
