class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = ""
        n = len(part)
        first = part[0]
        def remain(s):
            for i in range(len(s)):
                char = s[i]
                if char != first:
                    continue
                substring = s[i:i+n]
                if substring == part:
                    return s[:i] + s[i+n:]
            return s
        res = s
        for i in range(len(s)):
            new_res = remain(res)
            if new_res == res:
                break
            res = new_res

        return res