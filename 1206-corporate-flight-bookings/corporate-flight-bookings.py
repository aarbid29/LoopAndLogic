class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:

        ans = [0]*n

        for start ,end , value in bookings:

            ans[start-1] += value
            if end <n:
                ans[end]-=value
            
        #prefix sum 

        for i in range(1,len(ans)):
            ans[i] += ans[i-1]
        
        return ans


    

        





        


        

        







        