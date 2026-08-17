class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(root):
            if not root:
                return TreeNode(val)

            if val > root.val:
                root.right = dfs(root.right)

            elif val < root.val:
                root.left = dfs(root.left)

            return root

        return dfs(root)