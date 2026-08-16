class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None

            root_val = preorder[0]
            mid = inorder.index(root_val)

            node = TreeNode(root_val)

            node.left = dfs(
                preorder[1:mid + 1],
                inorder[:mid]
            )

            node.right = dfs(
                preorder[mid + 1:],
                inorder[mid + 1:]
            )

            return node

        return dfs(preorder, inorder)