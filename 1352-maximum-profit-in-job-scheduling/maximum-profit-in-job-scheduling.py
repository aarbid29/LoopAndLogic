
from functools import lru_cache

class Solution:
    def jobScheduling(self, startTime: list[int],
                      endTime: list[int],
                      profit: list[int]) -> int:

        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        starts = [job[0] for job in jobs]

        @lru_cache(None)
        def dfs(i):

            if i ==n:
                return 0 

            skip = dfs(i+1)

            bisect = bisect_left(starts , jobs[i][1])
            take =  jobs[i][2] + dfs(bisect)

            return max(skip,take)

        return dfs(0)