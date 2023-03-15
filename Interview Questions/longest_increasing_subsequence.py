import numpy as np
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        
        for i in range(1,len(nums)):
            for j in range(i): # check every number up until this point 
                if nums[i] > nums[j]: # to see if its larger than the current value
                    dp[i] = max(dp[i],dp[j]+1)

        return max(dp)


