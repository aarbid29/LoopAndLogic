class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        arr = [0] * len(nums)
        arr[0] = nums[0]
        for i in range(1, len(nums)):
            arr[i] = arr[i-1] + nums[i]
        
        minn = float("inf")

        for x in range(len(nums)):
            prefix = arr[x]
            for b in range(x-l+1, max(-1, x-r), -1):

                if b < 0:
                    break
                if b == 0:
                    calc = prefix
                else:
                    calc = prefix - arr[b-1]

                if calc > 0:
                    minn = min(minn, calc)

        return minn if minn != float("inf") else -1