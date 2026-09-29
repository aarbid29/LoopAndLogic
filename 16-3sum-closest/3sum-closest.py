class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        close = float("inf")

        nums.sort()


        for i in range(len(nums)-2):

            first  = nums[i]

            l = i+1
            r = len(nums)-1

            while l<r:

                add = first+ nums[l]+nums[r]

                diff = abs(target - add)

                if diff < abs(target - close):
                    close = add
                
                if add<target:
                    l+=1
                elif add>target:
                    r-=1
                else:
                    return target
        return close

            


        





        