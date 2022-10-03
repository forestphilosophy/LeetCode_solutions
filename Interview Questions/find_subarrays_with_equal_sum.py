class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = []
        
        for i in range(len(nums)-1):
            
            cur_num = nums[i]
            nxt_num = nums[i+1]
            
            _sum = cur_num + nxt_num 
            
            if _sum in sums:
                return True
            
            sums.append(_sum)
            
        return False
