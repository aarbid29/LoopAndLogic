from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp1 = Counter(t)
        mp2 = defaultdict(int)
        l = 0
        have = 0
        need = len(mp1)
        minn = float("inf")
        output = ""
        for r in range(len(s)):
            char = s[r]
            if char in mp1:
                mp2[char] += 1

                if mp2[char] == mp1[char]:
                    have += 1

            while have == need:
                if r - l + 1 < minn:
                    minn = r - l + 1
                    output = s[l:r + 1]
                left = s[l]
                
                if left in mp1:
                    mp2[left] -= 1
                    if mp2[left] < mp1[left]:
                        have -= 1
                l += 1

        return output