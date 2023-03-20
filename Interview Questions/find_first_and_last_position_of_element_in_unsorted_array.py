class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        loc = dict()
        loc['start'] = -1
        loc['end'] = -1

        seen = set()
        for idx,num in enumerate(nums):
            if num == target and (num not in seen):  
                loc['start'] = idx
                loc['end'] = idx
                seen.add(num)

            elif num == target and (num in seen):
                loc['end'] = idx

        return [loc['start'],loc['end']]


