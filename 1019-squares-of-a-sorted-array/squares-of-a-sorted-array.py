class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        mp = defaultdict(int)
        for num in nums:
            doub = num**2
            mp[doub]+=1

        res = []

        while mp:
            minn = min(mp)

            res.append(minn)
            mp[minn]-=1
            if mp[minn]==0:
                del mp[minn]

        return res

        

        