class Solution:
    def countElements(self, nums: List[int]) -> int:

        sorted_nums = sorted(nums)
        counter = 0

        if len(sorted_nums) <= 2:
            return 0
            
        for idx,num in enumerate(sorted_nums):
            remaining_l = sorted_nums.copy()
            remaining_l.pop(idx)
            if min(remaining_l) < num < max(remaining_l):
                counter += 1

        return counter

