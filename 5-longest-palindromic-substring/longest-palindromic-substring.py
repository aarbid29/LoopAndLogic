class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        res = ""
        res_len = 0

        for i in range(1 , len(s)):
            #odd lenght palin check:
            l= i
            r = i #starting with curr index i
            while s[l] == s[r]:
                l+=1
                r-=1
                if l == len(s) or r== -1:
                    break
            
            substring = s[r+1: l]
            if len(substring)> res_len:
                res =substring
                res_len = len(substring)
            
            #check for even now 
            l= i-1
            r= i
            while s[l] == s[r]:
                l+=1
                r-=1
                if l == len(s) or r== -1:
                    break
            
            substring = s[r+1: l]
            if len(substring)> res_len:
                res = substring
                res_len = len(substring)
        
        return res


