class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        @cache
        def dfs(r,c):
            
            Visited.add((r,c))
            if r == m - 1 and c == n - 1:
                return grid[r][c]

            if r < m - 1:
                sum1 = grid[r][c] + dfs(r+1,c) # move down

            else:
                sum1 = grid[r][c] + dfs(r,c+1) # we can only move right

            if c < n - 1:
                sum2 = grid[r][c] + dfs(r,c+1) # move right

            else:
                sum2 = grid[r][c] + dfs(r+1,c) # we can only move down

            return min(sum1,sum2)
        
        return dfs(0,0)
