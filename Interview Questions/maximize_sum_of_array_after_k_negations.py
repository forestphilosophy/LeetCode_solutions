class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        min_val_idx = nums.index(min(nums))
        nums[min_val_idx] = -nums[min_val_idx]  
        
        if k == 1:
   
            return sum(nums)
        
        else:
            
            return self.largestSumAfterKNegations(nums,k-1)
