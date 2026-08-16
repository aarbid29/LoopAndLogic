class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxx = float("-inf")

        def dfs(root):
            nonlocal maxx

            if not root:
                return 0

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            maxx = max(maxx, root.val + left + right)

            return root.val + max(left, right)

        dfs(root)
        return maxx