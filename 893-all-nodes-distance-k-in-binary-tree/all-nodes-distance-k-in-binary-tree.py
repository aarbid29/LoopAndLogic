from collections import defaultdict, deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []

        mp = defaultdict(lambda: None)

        def dfs(root, parent):
            if root is None:
                return

            mp[root] = parent

            dfs(root.left, root)
            dfs(root.right, root)

        dfs(root, None)

        dq = deque([(target, 0)])
        visited = {target}

        while dq:
            node, dist = dq.popleft()

            if dist == k:
                res.append(node.val)
                continue

            if node.left and node.left not in visited:
                visited.add(node.left)
                dq.append((node.left, dist + 1))

            if node.right and node.right not in visited:
                visited.add(node.right)
                dq.append((node.right, dist + 1))

            parent = mp[node]
            if parent and parent not in visited:
                visited.add(parent)
                dq.append((parent, dist + 1))

        return res