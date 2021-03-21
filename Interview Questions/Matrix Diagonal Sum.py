class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        
        primary = [mat[i][i] for i in range(len(mat))]
        secondary = []
        k = len(mat) - 1
        for i in range(len(mat)):
            if i == k:
                k -= 1
                continue
            secondary.append(mat[i][k])
            k -= 1
        return (sum(primary) + sum(secondary))
