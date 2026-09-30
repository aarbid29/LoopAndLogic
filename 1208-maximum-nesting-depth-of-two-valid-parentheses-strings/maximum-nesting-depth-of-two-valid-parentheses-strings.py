class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        stack = []

        for i, bracket in enumerate(seq):

            if bracket == ")":
                char, group = stack.pop()
                res.append(group)

            if bracket == "(":
                if stack:
                    char, group = stack[-1]

                    if group == 0:
                        stack.append((bracket, 1))
                        res.append(1)
                    else:
                        stack.append((bracket, 0))
                        res.append(0)

                    continue

                stack.append((bracket, 0))
                res.append(0)

        return res