class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[False]*n for i in range(m)]

        @cache
        def dfs(r,c):
            if r == m-1 or c == n-1:
                return 1

            move_right = dfs(r,c+1) # to the right

            move_down = dfs(r+1,c) # to the bottom

            return move_right + move_down

        return dfs(0,0)
