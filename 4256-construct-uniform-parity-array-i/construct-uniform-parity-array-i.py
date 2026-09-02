class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even_count = sum(1 for x in nums1 if x % 2 == 0)
        odd_count = sum( 1 for x in nums1 if x%2!= 0)
        n= len(nums1)
        if even_count == n:
            return True
        if odd_count ==n:
            return True
        
        if even_count >= odd_count:
            return True
        
        if odd_count>= even_count:
            return True
        return False


        

        



        