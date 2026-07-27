class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key= len)
        def helper(shorter, longer):
            if len(longer) != len(shorter) + 1:
                return False
            i = 0
            for c in longer:
                if i < len(shorter) and shorter[i] == c:
                    i += 1
            return i == len(shorter)

        dp = [1 for _ in range(len(words)+1)]

        for i in range(len(words)-1,-1,-1):
            maxx = 1 
            for j in range(i+1, len(words)):
                if helper(words[i],words[j]):
                    tmp = dp[j]+1
                    maxx = max(tmp,maxx)

            dp[i] = maxx
        return max(dp)