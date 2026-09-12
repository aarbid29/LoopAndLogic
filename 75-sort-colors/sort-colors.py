class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        k = 0 
        j = len(nums)-1
        # j holds the position for 2


        while k <= j :
            #k is scanning the array
            if nums[k]==2:
                nums[k],nums[j] = nums[j],nums[k]
                j-=1
                continue
            
            if nums[k]==0:
                nums[i],nums[k] = nums[k],nums[i]
                i+=1
            
            k+=1
            

            

            





        