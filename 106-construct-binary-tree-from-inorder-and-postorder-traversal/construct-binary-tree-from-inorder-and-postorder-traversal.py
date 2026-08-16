# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def dfs(inorder,postorder):
            if not postorder or not inorder:
                return None
            root_val = postorder[-1]

            indi = inorder.index(root_val)

            node = TreeNode(root_val)

            lenn = len(inorder[:indi])

            node.left = dfs(inorder[:indi], postorder[:lenn])

            node.right = dfs(inorder[indi+1:],  postorder[lenn:-1])

            return node

        return dfs(inorder , postorder)

        



        