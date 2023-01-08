class Solution:
    def canJump(self, nums: List[int]) -> bool:

        for i in reversed(range(len(nums))): # loop backwards to see if its reachable

            arr = nums[:i]
            for j in reversed(range(len(arr))):
                distance = i - j
                if nums[j] >= distance:
                    break
                
                else:
                    if j == 0: # reached the end
                        return False
        
        return True
