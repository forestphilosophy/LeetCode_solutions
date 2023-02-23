class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        
        for idx,i in enumerate(nums):
            
            if nums[idx] == 0:
                del nums[idx]
                nums.insert(0,0)

        if nums[0] == 0:
            insert_idx = len(nums) - nums[::-1].index(0)
        else:
            insert_idx = 0

        for idx,i in enumerate(nums):
            if nums[idx] == 1:
                del nums[idx]        
                nums.insert(insert_idx,1)

