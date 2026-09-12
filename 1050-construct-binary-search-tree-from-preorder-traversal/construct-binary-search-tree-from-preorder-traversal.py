# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:


        root = TreeNode(preorder[0])
        stack = [root]

        for i in range(1,len(preorder)):
            currr = preorder[i]
            curr = TreeNode(currr)

            if curr.val < stack[-1].val:
                stack[-1].left = curr

            else:
                parent = None

                while stack and stack[-1].val< curr.val:
                    parent = stack.pop()
                parent.right = curr
            
            stack.append(curr)
        
        return root
                
                











            



        