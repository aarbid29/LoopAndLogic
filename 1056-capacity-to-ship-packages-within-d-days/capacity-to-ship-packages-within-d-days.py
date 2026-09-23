class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        r = sum(weights)
        l = max(weights)
        
        while l <= r:

            mid = (r+l)//2
            #find num of days it would take for weight of the ship 
            day = 1
            runningsum = 0
            for weight in weights:

                if runningsum + weight >mid:
                    day+=1
                    runningsum = 0
                
                runningsum += weight
            
            if day > days:
                l = mid + 1
            else:
                r= mid -1
                
        return l
            




