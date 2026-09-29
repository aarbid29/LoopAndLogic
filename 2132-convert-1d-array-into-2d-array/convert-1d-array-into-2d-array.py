class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []
        res = []
        build = []
        le = 0

        for num in original:
            build.append(num)
            le += 1

            if le == n:
                res.append(build)
                le = 0
                build = []

        return res