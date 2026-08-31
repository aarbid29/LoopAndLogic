class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0 
        count = 0 

        for i in range(len(flowerbed)):

            if flowerbed[i]==1:
                prev = flowerbed[i]
                continue
        
            if i==len(flowerbed)-1 and prev==0:
                count+=1
                continue
            if prev==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                count+=1
        
            prev = flowerbed[i]


        return count>=n
            

            

        
        

            




        