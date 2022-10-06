# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _is_leaf(self, node):
        
        if not node.left and not node.right:
            return True
        
        return False
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if not root.left and not root.right:
            return 0
        
        else:
            
            if not root.left and root.right:
                if self._is_leaf(root.right):
                    return 0
                
                return self.sumOfLeftLeaves(root.right)
            
            elif root.left and not root.right:
                if self._is_leaf(root.left):
                    return root.left.val
                
                return self.sumOfLeftLeaves(root.left)
            
            if self._is_leaf(root.right) and self._is_leaf(root.left):
                return root.left.val
            
            elif self._is_leaf(root.right) and not self._is_leaf(root.left):
                return self.sumOfLeftLeaves(root.left)
            
            elif not self._is_leaf(root.right) and self._is_leaf(root.left):
                return root.left.val + self.sumOfLeftLeaves(root.right)
            
            elif not self._is_leaf(root.right) and not self._is_leaf(root.left):
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
                
