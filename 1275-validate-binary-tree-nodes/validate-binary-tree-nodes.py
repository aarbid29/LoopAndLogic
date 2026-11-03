class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        adj = defaultdict(list)
        for i in range(len(leftChild)):
            adj[i].append(leftChild[i])
            adj[i].append(rightChild[i])

        visited = set()

        def dfs(node):
            if node in visited:
                return False

            visited.add(node)
            for neigh in adj[node]:
                if neigh == -1:
                    continue
                if not dfs(neigh):
                    return False
            return True
        #find node with indegree 0  , i.e the root 
        indegree = [0] * n

        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1

            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1
        root = -1
        for i in range(n):
            if indegree[i] == 0:
                if root != -1:
                    return False  # more than one root
                root = i

        if root == -1:
            return False  # no root

        if not dfs(root):
            return False
        else:
            return n == len(visited)