class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_strs = [''.join(sorted(i)) for i in strs]

        groups = set(sorted_strs)

        ans = [[] for i in range(len(groups))]

        _dict = {k:idx for idx,k in enumerate(groups)}

        for i in strs:
            ans[_dict[''.join(sorted(i))]].append(i)

        return ans

