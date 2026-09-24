class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        mp = defaultdict(list)
        for i , char in enumerate(t):
            mp[char].append(i)
        prev = -1
        def check(i):
            nonlocal prev
            postion = mp[i]
            idx = bisect_left(postion, prev)

            if idx == len(postion):
                return False
            
            prev = postion[idx]+1

            return True
        

        for i,char in enumerate(s):
            if not check(char):
                return False
        return True


        