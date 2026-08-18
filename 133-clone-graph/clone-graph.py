class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {}

        def dfs(node):
            if node in mp:
                return mp[node]

            new_node = Node(node.val)
            mp[node] = new_node

            for neigh in node.neighbors:
                new_node.neighbors.append(dfs(neigh))

            return new_node

        if not node:
            return None

        return dfs(node)