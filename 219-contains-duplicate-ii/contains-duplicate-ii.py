class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        l = 0 
        seen = set()
        mp  = defaultdict()
        
        for r in range(len(nums)):
            while nums[r] in seen:
                left = nums[l]
                if left == nums[r]:
                    calc = abs(r-l)
                    if calc<=k:
                        return True
                l+=1
                seen.remove(left)
            seen.add(nums[r])
        return False

                

        