class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 1
        for i in range(1,len(s)):
            #odd lenght palin check:
            l= i
            r = i #starting with curr index i
            while s[l] == s[r]:
                count+=1
                l-=1
                r+=1
                if r == len(s) or l== -1:
                    break

            
            #check for even now 
            l= i-1
            r= i
            while s[l] == s[r]:
                count+=1
                l-=1
                r+=1
                if r == len(s) or l== -1:
                    break

        return count



        