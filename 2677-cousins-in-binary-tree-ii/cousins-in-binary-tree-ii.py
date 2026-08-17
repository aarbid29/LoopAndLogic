class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        dq = deque([(root, None)])

        level_sum = defaultdict(int)
        child_sum = defaultdict(int)
        lvl = 0

        while dq:
            size = len(dq)
            for _ in range(size):
                node, parent = dq.popleft()

                level_sum[lvl] += node.val

                if node.left:
                    dq.append((node.left, node))

                if node.right:
                    dq.append((node.right, node))

            lvl += 1

        dq = deque([(root, None)])

        while dq:
            size = len(dq)
            for _ in range(size):
                node, parent = dq.popleft()

                if node.left:
                    child_sum[node] += node.left.val
                    dq.append((node.left, node))

                if node.right:
                    child_sum[node] += node.right.val
                    dq.append((node.right, node))
        parent = None

        def dfs(root, i, parent):
            if parent is None:
                root.val = 0
            else:
                root.val = level_sum[i] - child_sum[parent]
                
            if root.left:
                dfs(root.left, i + 1, root)

            if root.right:
                dfs(root.right, i + 1, root)


        dfs(root, 0, None)
        return root