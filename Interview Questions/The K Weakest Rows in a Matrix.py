class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = {}
        for i in range(len(mat)):
            result[i] = mat[i].count(1)
        
        result = sorted(result.items(), key=lambda x: (x[1], x[0]))
        return ([result[i][0] for i in range(k)])
