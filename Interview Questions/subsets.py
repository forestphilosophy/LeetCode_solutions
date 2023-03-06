class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]

        _len = 1
        while _len <= len(nums):

            l = list(itertools.combinations(nums, _len))
            for i in l:
                ans += [list(i)]

            _len += 1

        return ans




