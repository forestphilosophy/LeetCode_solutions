class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        def dfs(r,c,word):

            Visited.add((r,c))
            up = board[r-1][c] if r >= 1 else False
            down = board[r+1][c] if r <= m-2 else False
            left = board[r][c-1] if c >= 1 else False
            right = board[r][c+1] if c <= n-2 else False
            
            if len(word) == 1: # found the last letter
                return True

            if up != word[1] and down != word[1] and left != word[1] and right != word[1]:
                return False

            if up == word[1] and (r-1,c) not in Visited:
                if dfs(r-1,c,word[1:]):
                    return True
                Visited.remove((r-1,c))

            if down == word[1] and (r+1,c) not in Visited:
                if dfs(r+1,c,word[1:]):
                    return True           
                Visited.remove((r+1,c))

            if left == word[1] and (r,c-1) not in Visited:
                if dfs(r,c-1,word[1:]):
                    return True
                Visited.remove((r,c-1))

            if right == word[1] and (r,c+1) not in Visited:
                if dfs(r,c+1,word[1:]):
                    return True
                Visited.remove((r,c+1))

        for r in range(m):
            for c in range(n):
                Visited = set()
                if board[r][c] == word[0]:
                    if dfs(r,c,word):
                        return True

        return False
