from collections import defaultdict

class Solution:
    def list_duplicates(self,seq):
        tally = defaultdict(list)
        for i,item in enumerate(seq):
            tally[item].append(i)
            
        return ([key,[t - s for s, t in zip(locs, locs[1:])]] for key,locs in tally.items() 
                                if len(locs)>1)
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        res = sorted(self.list_duplicates(nums))
        
        for dup in res:
            if any(diff <= k for diff in dup[1]):
                return True
    
            
        return False
