class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0 
        mp = defaultdict(int)
        maxx = 0

        for r in range(len(s)):
            curr = s[r]
            mp[curr]+=1

            while mp[curr]>2:
                rem = s[l]
                mp[rem]-=1
                l+=1
            maxx = max(maxx,r-l+1)

        return maxx

        