# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0 

        def dfs(root):
            nonlocal count
            if not root:
                return (0,0,0) 
            # total_summ = 0
            # total_elements= 0
        
            root_val, summ , ele= dfs(root.left)
            root_val2 , summ2,ele2 = dfs(root.right)
        
            #after getting value from its left child and right child
            #calculate avg and check
            total_elements = ele + ele2 + 1
            total_summ = summ + summ2 + root.val
            avg = total_summ//total_elements

            if avg == root.val:
                count+=1
            return root.val ,total_summ , total_elements
        
        dfs(root)
        return count



            










        