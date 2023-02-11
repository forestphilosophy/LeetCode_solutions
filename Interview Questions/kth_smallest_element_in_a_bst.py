# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        l = []

        def dfs(node):

            if not node:
                return

            l.append(node.val)

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

        dfs(root)

        return sorted(l)[k-1]
