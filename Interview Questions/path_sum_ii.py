# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        output = []
        path = []

        def dfs(node,path,output,Sum):
            
            if not root:
                return

            path.append(node.val) # adding the value into the path
            print(path)
            if not node.left and not node.right and node.val == Sum: # we got a leaf node:          
                output.append(list(path))
                
            if node.left:
                dfs(node.left,path,output,Sum-node.val)

            if node.right:
                dfs(node.right,path,output,Sum-node.val)

            path.pop() # backtracking

        dfs(root,path,output,targetSum)
        return output

            


        
