class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []

        if numRows == 0:
            return arr

        arr.append([1])

        def dfs(row):
            if row == numRows:
                return

            prev = arr[-1]
            build = [1]

            for i in range(1, len(prev)):
                build.append(prev[i - 1] + prev[i])

            build.append(1)
            arr.append(build)

            dfs(row + 1)

        dfs(1)
        return arr
