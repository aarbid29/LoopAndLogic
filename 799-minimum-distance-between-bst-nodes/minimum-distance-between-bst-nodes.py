# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minn = float("inf")
        prev = None

        def dfs(root):
            nonlocal minn,prev

            if not root:
                return 

            dfs(root.left)
            if prev is not None:
                minn = min(minn, root.val - prev)

            prev = root.val

            dfs(root.right)

        dfs(root)
        return minn








        