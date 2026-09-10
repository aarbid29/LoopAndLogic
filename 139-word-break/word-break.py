class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in word_set:
                length = len(word)

                if length <= i and dp[i - length]:
                    if s[i - length:i] == word:
                        dp[i] = True
                        break

        return dp[n]