class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        first = -1
        
        def dfs(i, j):
            nonlocal first
            
            if i >= len(haystack):
                return
            
            if j >= len(needle):
                return
            
            if haystack[i] == needle[j]:
                if haystack[i:i+len(needle)] == needle:
                    first = i
                    return
            dfs(i + 1, 0)

        dfs(0, 0)
        return first