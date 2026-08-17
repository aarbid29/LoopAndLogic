# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

  
        def dfs(root):
            nonlocal total
            if not root:
                return 
            
            right = dfs(root.right)

            old = root.val
            root.val =  old + total
            total += old
            
            dfs(root.left)

        dfs(root)
        return root


        



            
        





        