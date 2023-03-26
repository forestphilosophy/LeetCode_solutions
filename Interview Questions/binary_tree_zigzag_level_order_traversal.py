# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dp = defaultdict(list)
        def bfs(node,level=0):
            
            if not node:
                return 

            dp[level].append(node.val)

            if not node.left and not node.right:
                return

            if node.left:
                bfs(node.left,level=level+1)

            if node.right:
                bfs(node.right,level=level+1)

        bfs(root)

        flip = False
        ans = []
        for i in range(len(dp)):
            if not flip:
                ans.append(dp[i])
                flip = True

            else:
                ans.append(list(reversed(dp[i])))
                flip = False


        return ans

