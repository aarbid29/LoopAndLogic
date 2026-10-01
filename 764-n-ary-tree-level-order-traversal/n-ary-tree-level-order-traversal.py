"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        res = []
        build = []

        dq = deque([root])

        while dq:
            size = len(dq)
            build = []

            for _ in range(size):
                node = dq.popleft()

                build.append(node.val)

                if node.children is not None:
                    for n in node.children:
                        dq.append(n)
                
            res.append(build)
        return res

        