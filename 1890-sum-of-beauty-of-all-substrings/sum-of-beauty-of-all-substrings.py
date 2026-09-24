class Solution:
    def beautySum(self, s: str) -> int:
        sett =[]
        #generate all substrings 
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sett.append(s[i:j])
        beauty = 0
        for word in sett:
            freq = Counter(word)

            beauty+=(max(freq.values()) - min(freq.values()))
            max(freq.values()) - min(freq.values())
        return beauty
        



        