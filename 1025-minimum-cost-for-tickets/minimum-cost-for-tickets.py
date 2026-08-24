class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}
        def dfs(i,day):
            if (i,day)in cache:
                return cache[(i,day)]
            if i >= len(days):
                return 0
            # if i==len(days)-1 and day> days[i]:
            #     return 0            
            if days[i]<=day:
                cache[i,day] = dfs(i+1,day)
                return cache[i,day] 
        
            if days[i]>day:
                day1 = costs[0] + dfs(i+1,days[i])
                day7= costs[1] + dfs(i+1,days[i]+6)
                day30 = costs[2] + dfs(i+1,days[i]+29)
                low = min(day1,day7,day30)
                cache[(i,day)] = low
                return low
        return dfs(0,0)
                

        