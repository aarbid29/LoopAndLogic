# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(array):
            if not array:
                return None


            midd = len(array)//2
            val = array[midd]
            node = TreeNode(val)

            node.left = dfs(array[:midd])

            node.right = dfs(array[midd+1:])

            return node

        
        return dfs(nums)


  






        
        