class Solution:
    def findGCD(self, nums: List[int]) -> int:

        nums = sorted(nums)
        _min = nums[0]
        _max = nums[-1]

        if _min == _max or (_min == 2 and _max % _min == 0) or _min == 1:
            return _min

        ans = _min
        while ans > 0:
            if _max % ans == 0 and _min % ans == 0:
                return ans

            ans -= 1
        
        return ans
