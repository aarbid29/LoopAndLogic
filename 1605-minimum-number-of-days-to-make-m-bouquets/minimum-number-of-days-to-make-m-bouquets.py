class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n =  len(bloomDay)
        if n < m * k:
            return -1
        l = 0 
        maxx = max(bloomDay)
        r = maxx

        while l<r :
            midd = (l+r)//2
            time = 0 
            i = 0 
            boq = 0 

            #can m boq be made with midd-> day?
            while i<n:
                flower = bloomDay[i]
                adj = 0 

                while i < n and bloomDay[i]<=midd:
                    adj+=1
                    i+=1
                    if adj == k:
                        boq+=1
                        break
                if i < n and bloomDay[i] > midd:
                    i+=1
                
            if boq < m:
                l = midd + 1
            else:
                r = midd 
        
        return l

                

                







        

        

        