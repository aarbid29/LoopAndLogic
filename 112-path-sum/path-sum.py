class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        found = False

        def dfs(root, summ):
            nonlocal found

            if not root:
                return

            summ += root.val

            if not root.left and not root.right:
                if summ == targetSum:
                    found = True
                return

            dfs(root.left, summ)
            dfs(root.right, summ)

        dfs(root, 0)

        return found