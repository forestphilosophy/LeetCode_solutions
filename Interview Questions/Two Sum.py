class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if i == len(nums):
                continue
            else:
                remaining_arr = nums[i+1:]
                for j in range(len(remaining_arr)):
                    if nums[i] + remaining_arr[j] == target:
                        return [i,i+j+1]
