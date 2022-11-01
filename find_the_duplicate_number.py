class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = defaultdict(lambda:False)
        
        for num in nums:
            
            if seen[num] == True:
                return num
            
            seen[num] = True
