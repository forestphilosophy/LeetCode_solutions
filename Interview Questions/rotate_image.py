class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        tmp = [[None] * n for i in range(n)]

        for i in range(n):
            tmp[i] = list(reversed([matrix[r][i] for r in range(n)]))

        for i in range(n):
            for j in range(n):
                matrix[i][j] = tmp[i][j]
