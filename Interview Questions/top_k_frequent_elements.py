class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ans = {}

        for i in nums:
            if i not in ans:
                ans[i] = 0 

            else:
                ans[i] += 1

        ans = dict(sorted(ans.items(), key=lambda item: item[1]))

        return list(ans.keys())[-k:]
