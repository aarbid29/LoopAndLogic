class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        track = 0
        def calc(z,o):
            nonlocal track
            prevz = s[z]
            prevo = s[o]
            #expand from , need of index
            while z>=0 and o<len(s) and s[z]==prevz and s[o]==prevo:
                track+=1
                prevz = s[z]
                prev0 = s[o]
                z-=1
                o+=1
            return



        
        for i in range(len(s)):
            if  i == len(s)-1:
                continue
            curr  = s[i]
            nextt = s[i+1]
            if (curr == "0"and nextt=="1") or (curr == "1"and nextt=="0"):
                # track+=1
                calc(i,i+1)
        return track
            

           