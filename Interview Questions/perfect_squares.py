class Solution:
    def numSquares(self, n: int) -> int:
        
        tmp = defaultdict(bool)
        def find_sr(n):
            perfect_sr = []
            for i in range(n,0,-1):
                sr = int(math.sqrt(i))
                if (sr*sr) == i:
                    perfect_sr.append(i)
                    tmp[i] = True

            return perfect_sr
                    
        perfect_sr = find_sr(n)

        @cache
        def helper(n):
            
            if tmp[n]:
                return 1

            return min([1+helper(n-i) for i in perfect_sr if n-i > 0])

        return helper(n)

            

            
