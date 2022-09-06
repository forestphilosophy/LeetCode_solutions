class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = 0
        
        for num in nums:
            if num != target and num < target:
                pos += 1
            
            elif num == target or num > target:
                return pos
            
        return pos
