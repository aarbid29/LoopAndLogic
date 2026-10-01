# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []

        def dfs( node , build,currsum):
    
            if not node:
                return 
            
            build.append(node.val)
            currsum+=node.val

            if not node.left and not node.right:
                if currsum ==targetSum:
                    res.append(build.copy())
                build.pop()
                return



            dfs(node.left , build,currsum)
            dfs(node.right,build,currsum)

            build.pop()

        
        dfs(root,[],0)
        return res
            

            
            



            
        