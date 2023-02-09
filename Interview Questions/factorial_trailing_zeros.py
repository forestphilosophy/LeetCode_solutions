import numpy as np
class Solution:
    def trailingZeroes(self, n: int) -> int:

        num = str(np.math.factorial(n))
        
        ans = 0
        #print(num)

        if len(num) == 1:
            if num[0] == '0':
                return 1
            else:
                return 0

        for i in range(len(num)-1,0,-1):
            #print(i)
            #print(num[i])
            if num[i] != '0':
                return ans

            if num[i] == '0':
                ans += 1

        return ans
