class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        dup_idx = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                dup_idx.append(i+1)
                     
        for index in sorted(dup_idx, reverse=True):
            del nums[index]   
            
        k = len(nums)
        
        return k
