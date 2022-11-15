class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        combo_l = list(itertools.combinations(arr, 2))
        
        frac_l = [[[i[0],i[1]],i[0]/i[1]] for i in combo_l]
        
        frac_l.sort(key=lambda x:x[1])
        
        return frac_l[k-1][0]
