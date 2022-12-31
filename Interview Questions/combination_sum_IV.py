class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = {}

        def some_func(nums,target):

            if target == 0:
                return 0 

            if target in dp:
                return dp[target]

            combos = 0
            for num in nums:
                if target - num < 0:
                    continue
                
                elif target - num == 0:
                    combos += 1
                
                elif target - num > 0:
                    combos += some_func(nums,target-num)

            dp[target] = combos

            return combos
        
        some_func(nums,target)

        return dp[target]
