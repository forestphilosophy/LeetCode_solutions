class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)

        @cache
        def good(idx):
            if idx == N: # reached the end of array
                return True

            if idx + 1 < N and nums[idx] == nums[idx+1] and good(idx+2):
                return True

            if idx + 2 < N and nums[idx] == nums[idx+1] == nums[idx+2] and good(idx+3):
                return True

            if idx + 2 < N and nums[idx] == nums[idx+1] - 1 and nums[idx+1] == nums[idx+2] - 1 and good(idx+3):
                return True

            return False

        return good(0)




        
