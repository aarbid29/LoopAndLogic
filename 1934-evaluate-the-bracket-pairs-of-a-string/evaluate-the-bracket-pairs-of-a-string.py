class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = defaultdict(str)
        for key ,val in knowledge:
            mp[key] = val
        n = len(s)
        l = 0 

        res = ""
        i = 0

        while i < len(s):
            if s[i]!= "(":
                res+=s[i]
                i+=1
            else:
                r = i
                l =i
                while r < len(s) and s[r]!=")":
                    r+=1
                
                word = s[l+1:r]
                if word in mp:
                    replace = mp[word]
                else:
                    replace = "?"

                res+=replace
                i = r+1
                continue
        return res







        

        

        