class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        res.sort()

        i = 0

        def dfs(root):
            nonlocal i
            if not root:
                return

            dfs(root.left)

            root.val = res[i]
            i += 1

            dfs(root.right)

        dfs(root)