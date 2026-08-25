class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxx = 0

        def dfs(node):
            nonlocal maxx

            if node is None:
                return True, 0, float("inf"), float("-inf")

            leftbst, left_sum, left_low, left_high = dfs(node.left)
            rightbst, right_sum, right_low, right_high = dfs(node.right)

            if leftbst and rightbst and left_high < node.val < right_low:

                total = left_sum + right_sum + node.val
                maxx = max(maxx, total)

                return (
                    True,
                    total,
                    min(left_low, node.val),
                    max(right_high, node.val)
                )

            return False, 0, 0, 0

        dfs(root)
        return maxx
