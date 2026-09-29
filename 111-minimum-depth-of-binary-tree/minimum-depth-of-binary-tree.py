# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return float("inf")
            
            left = dfs(node.left)
            right = dfs(node.right)

            minn = min(left,right)
            if minn == float("inf"):
                minn=0
            return minn+1
        
        return dfs(root)


        