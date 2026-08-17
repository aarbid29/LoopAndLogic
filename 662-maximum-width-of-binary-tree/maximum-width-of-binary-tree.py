class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        dq = deque([(root, 0)])
        maxx = 0

        while dq:
            size = len(dq)

            first = dq[0][1]
            last = dq[-1][1]

            maxx = max(maxx, last - first + 1)

            for _ in range(size):
                node, idx = dq.popleft()

                if node.left:
                    dq.append((node.left, 2 * idx))

                if node.right:
                    dq.append((node.right, 2 * idx + 1))

        return maxx