# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def dfs(root):
            if not root:
                return None
            
            root_right = root.right

            root.right = dfs(root.left)
            root.left = None

            curr = root
            while curr.right:
                curr = curr.right
            curr.right = root_right            

            dfs(root_right)

            return root
        return dfs(root)





        