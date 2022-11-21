"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
        
        if not root.children:
            return 1
        
        depth_list = []
        
        for child in root.children:
            
            child_depth = self.maxDepth(child)
            
            depth_list.append(child_depth+1)
            
        max_depth = max(depth_list)
        
        return max_depth
