# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        

        def dfs(arr):
            if not arr:
                return

            maxx = max(arr)
            maxidx = arr.index(maxx)
            node = TreeNode(maxx)
            node.left = dfs(arr[:maxidx])
            node.right = dfs(arr[maxidx+1:])

            return node

        return dfs(nums)






        