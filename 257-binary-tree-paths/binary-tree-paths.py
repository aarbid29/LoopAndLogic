class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        res = []

        def backtrack(node, sol):
            if not node:
                return

            sol.append(str(node.val))

            if not node.left and not node.right:
                res.append("->".join(sol))

            backtrack(node.left, sol)
            backtrack(node.right, sol)

            sol.pop()

        backtrack(root, [])

        return res