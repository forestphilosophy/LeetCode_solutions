class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(grid,r,c):
            if (r < 0 or c < 0 or r >= rows or c >= cols) or grid[r][c] != '1': # not a land or out of bounds    
                return 

            grid[r][c] = 'V' # V for visited

            # run dfs on all adjcent cells
            dfs(grid,r-1,c) # up
            dfs(grid,r+1,c) # down
            dfs(grid,r,c-1) # left
            dfs(grid,r,c+1) # right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(grid,r,c)
                    islands += 1

        return islands
