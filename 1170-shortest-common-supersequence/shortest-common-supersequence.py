class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        n = len(str2)

        prev = [str2[j:] for j in range(n)]
        prev.append("")

        for i in range(len(str1) - 1, -1, -1):

            curr = [""] * (n + 1)
            curr[n] = str1[i:]

            for j in range(n - 1, -1, -1):

                if str1[i] == str2[j]:
                    curr[j] = str1[i] + prev[j + 1]

                else:
                    res1 = str1[i] + prev[j]
                    res2 = str2[j] + curr[j + 1]

                    if len(res1) <= len(res2):
                        curr[j] = res1
                    else:
                        curr[j] = res2

            prev = curr

        return prev[0]