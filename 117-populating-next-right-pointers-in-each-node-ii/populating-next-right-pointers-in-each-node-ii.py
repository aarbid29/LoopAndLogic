class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        dq = deque([root])

        while dq:
            size = len(dq)
            for i in range(size):
                node= dq.popleft()
                second_node = dq[0] if dq else None
                if i == size-1:
                    node.next = None
                else:
                    node.next = second_node
    
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        
        return root