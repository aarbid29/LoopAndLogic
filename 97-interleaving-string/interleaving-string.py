class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
             return False

        # k is the index of s3
        # i is for s1 and j is for s2
        @lru_cache(None)
        def dfs(i,j,k):
            if k == len(s3):
                return True

            if i == len(s1):
                return s2[j:] == s3[k:]

            if j == len(s2):
                return s1[i:] == s3[k:]

            if s1[i]==s2[j]==s3[k]:

                first = dfs(i+1,j,k+1)
                second = dfs(i,j+1,k+1)

                return first or second

            if s1[i]==s3[k]:
                return dfs(i+1,j,k+1)
            
            if s2[j] == s3[k]:
                return dfs(i,j+1,k+1)
            
            return False
                

        return dfs(0,0,0)
            
            
