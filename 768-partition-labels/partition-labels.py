class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp= defaultdict(int)
        res = []
        for i in range(len(s)-1,-1,-1):
            char = s[i]
            if char not in mp :
                mp[char] = i
        l= 0
        while l<len(s):
            char = s[l]
            lenght = mp[char]
            i = l
            while i<=lenght:
                lenght = max(lenght,mp[s[i]])
                i+=1
            res.append(lenght-l+1)

            l=lenght+1

        return res


        



            
        










        
        