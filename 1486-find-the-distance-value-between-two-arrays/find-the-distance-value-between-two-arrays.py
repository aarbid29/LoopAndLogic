class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        valid = 0 
        for num in arr1:
            idx = bisect_left(arr2, num)

            #check for idx  and check for elemnt before idx
            if idx-1 >=0 and idx < len(arr2):#check for both index lies within bound
                if abs(num - arr2[idx-1] )>d and abs(arr2[idx]- num)>d:
                    valid+=1
                    continue

            if idx >=len(arr2):
                if abs(arr2[idx-1]-num)>d:
                    valid+=1
                    continue
            if not (idx-1)>=0:
                if abs(arr2[idx]- num)>d:
                    valid+=1
                    continue
                    

        return valid



