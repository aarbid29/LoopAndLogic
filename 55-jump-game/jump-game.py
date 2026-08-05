class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached = [False] * (len(nums) + 1)
        reached[len(nums)-1] = True
        prev_true = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= prev_true:
                prev_true = i
                reached[i] = True
            else:
                reached[i] = False

        return reached[0]