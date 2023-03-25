class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m,n = len(matrix),len(matrix[0])
        Visited = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and (i,j) not in Visited:
                    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        x = i
                        y = j

                        while True:
                            x += dx
                            y += dy

                            if x < 0 or x >= m or y < 0 or y >= n:
                                break
                                
                            if matrix[x][y] != 0 and (x,y) not in Visited:
                                Visited.add((x,y))
                                matrix[x][y] = 0
