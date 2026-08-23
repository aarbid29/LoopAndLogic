class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp_len = [1 for _ in range(n)]
        dp_count = [1 for _ in range(n)]
        #first phase , calculating LIS
        for i in range(n - 1, -1, -1):
            maxx = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    tmp = dp_len[j] + 1
                    maxx = max(tmp, maxx)
            dp_len[i] = maxx
        
        #second phase , calculating max count 

        for i in range(n - 1, -1, -1):
            cnt = 0
            for j in range(i + 1, n):
                if nums[j] > nums[i] and dp_len[j] + 1 == dp_len[i]:
                    cnt += dp_count[j]
            if cnt == 0:
                cnt = 1

            dp_count[i] = cnt
        #highest count of max len
        longest = max(dp_len)
        ans = 0

        for i in range(n):
            if dp_len[i] == longest:
                ans += dp_count[i]

        return ans
        

        




            








        