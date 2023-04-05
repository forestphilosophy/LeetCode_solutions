class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates = sorted(candidates)
        Visited = set()

        def helper(candidates,target,path):

            if tuple(candidates) in Visited:
                return
            
            Visited.add(tuple(candidates))
            
            if target == 0:
                res.add(tuple(sorted(path)))
                return 

            if target < 0 or len(candidates) == 0:
                return

            for i in range(len(candidates)):
                new_candidates = candidates[:i] + candidates[i+1:]
                path += [candidates[i]]
                helper(new_candidates,target-candidates[i],path)
                path.pop(-1)

        helper(candidates,target,[])
        return res


        
          
