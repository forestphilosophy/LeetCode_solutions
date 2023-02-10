# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node):
            return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))
        
        height = get_height(root)
        m = height
        n = 2**(height) - 1

        res = [[""] * n for i in range(m)]
    
        def dfs(node,r,c):
            res[r][c] = str(node.val)
            
            if node.left:
                dfs(node.left,r+1,int(c-2**(height-r-2)))

            if node.right:
                dfs(node.right,r+1,int(c+2**(height-r-2)))

        dfs(root,r=0,c=int(n/2))

        return res

