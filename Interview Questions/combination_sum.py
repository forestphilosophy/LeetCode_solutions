class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        def dfs(candidates,target,steps=[]):
            if target == 0:
                steps = sorted(steps)
                if steps not in ans:
                    ans.append(steps)

                return steps

            if target < 0:
                return []

            for i in candidates:
                dfs(candidates,target-i,steps=steps+[i])

        dfs(candidates,target)

        return ans

