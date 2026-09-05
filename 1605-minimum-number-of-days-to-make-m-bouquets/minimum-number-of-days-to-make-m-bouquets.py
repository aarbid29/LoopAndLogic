class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        l = 1 
        r = max(bloomDay)
        while l < r :
            day = (l+r)//2
            cnt = 0
            i = 0
            boq = 0 
            while i < len(bloomDay):
                if bloomDay[i] <= day:
                    cnt += 1
                    if cnt == k:
                        boq += 1
                        cnt = 0
                    i += 1
                else:
                    cnt = 0
                    i += 1

            if boq >=m:
                r= day
            else:
                l = day +1 
        return l
                
                
                
                









            
                
















        