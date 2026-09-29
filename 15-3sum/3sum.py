class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            first = nums[i]

            k = i + 1
            j = len(nums) - 1

            while k< j:

                add = nums[j] + nums[k] + first

                if add ==0:
                    res.add(tuple([nums[i], nums[k], nums[j]]))
                    k+=1
                    j-=1
                    continue
                
                if add >0:
                    j-=1
                elif add<0:
                    k+=1
                else:
                    continue


        outt = []
        for h in res:
            outt.append(list(h))
        return outt