from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        mp = defaultdict(int)
        for char in "balon":
            mp[char] = 0

        for char in text:
            if char in "balon":
                mp[char] += 1

        mp["l"] //= 2
        mp["o"] //= 2

        min_key = min(mp, key=mp.get)

        return mp[min_key]