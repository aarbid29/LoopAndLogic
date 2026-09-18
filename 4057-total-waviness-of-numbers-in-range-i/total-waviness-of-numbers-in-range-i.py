class Solution:
    def totalWaviness(self, low: int, high: int) -> int:

        @lru_cache(None)
        def waviness(s, i=1):
            if i == len(s) - 1:
                return 0

            if s[i - 1] < s[i] > s[i + 1]:
                return 1 + waviness(s, i + 1)

            if s[i - 1] > s[i] < s[i + 1]:
                return 1 + waviness(s, i + 1)

            return waviness(s, i + 1)

        total = 0

        for num in range(low, high + 1):
            s = tuple(map(int, str(num)))

            if len(s) >= 3:
                total += waviness(s)

        return total
