class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [-1] * len(nums)
        dp[n-1] = 0

        for i in range(n-1,-1,-1):
            reachables = [i + j for j in range(1,nums[i]+1) if i + j < n]

            if len(reachables) == 0:
                continue

            l = [1+dp[idx] for idx in reachables if dp[idx] != -1]

            dp[i] = min(l) if len(l) != 0 else -1

        return dp[0]
