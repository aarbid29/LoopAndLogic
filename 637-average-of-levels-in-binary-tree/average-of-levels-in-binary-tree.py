# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:

        res = [] 

        dq = deque([root])
        while dq :
            size = len(dq)
            summ = 0
            div = size

            for _ in range(size):
                node = dq.popleft()
                summ+= node.val

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            res.append(summ/div)
        return res




        