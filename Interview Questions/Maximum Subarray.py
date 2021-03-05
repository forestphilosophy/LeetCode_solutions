#Solution 1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maximum_sum = 0
        
        if len(nums) == 1:
            return nums[0]
        
        elif all(num < 0 for num in nums):
            return max(nums)
        
        else:
            for i in range(0,len(nums)):
                for j in range(i+1,len(nums)+1):
                    if sum(nums[i:j]) > maximum_sum:
                        maximum_sum = sum(nums[i:j])
        
        return maximum_sum

#Solution 2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1,n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
