# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ancestors = defaultdict(list)
        ancestors_dict = defaultdict(TreeNode)
        def dfs(node,ancestors):
            if not node:
                return

            ancestors[node.val].append(node.val)
            ancestors_dict[node.val] = node
            if node.left:
                ancestors[node.left.val].extend(ancestors[node.val])
                dfs(node.left,ancestors)

            if node.right:
                ancestors[node.right.val].extend(ancestors[node.val])
                dfs(node.right,ancestors)

        dfs(root,ancestors)
        
        if p.val in ancestors[q.val]:
            return ancestors_dict[p.val]

        elif q.val in ancestors[p.val]:
            return ancestors_dict[q.val]

        len_p,len_q = len(ancestors[p.val]),len(ancestors[q.val])

        if len_p >= len_q:
            for ances in reversed(ancestors[q.val]):
                if ances in ancestors[p.val]:
                    return ancestors_dict[ances] 

        else:
            for ances in reversed(ancestors[p.val]):
                if ances in ancestors[q.val]:
                    return ancestors_dict[ances]
