class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # gather all info about string "t"
        mp = Counter(t)
        formed_check = len(mp)

        # for window's mp
        mp2 = defaultdict(int)
        l = 0
        minn = float("inf")
        formed = 0
        res = ""

        for r in range(len(s)):
            if s[r]not in mp:
                continue
            
            mp2[s[r]]+=1
            curr = s[r]
            if mp2[curr]==mp[curr]:
                formed+=1
            
            while formed == formed_check:

                while l<r and s[l] not in mp:
                    l+=1
                
                length = r-l+1
                if length< minn:
                    res = s[l:r+1]
                    minn = length 

                left = s[l]
                mp2[left]-=1

                if mp2[left]<mp[left]:
                    formed-=1
                
                l+=1
        return res


