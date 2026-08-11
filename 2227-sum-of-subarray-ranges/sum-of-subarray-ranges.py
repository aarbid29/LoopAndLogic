class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        # next smaller element
        nse = [n] * n
        stack = []

        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                index = stack.pop()
                nse[index] = i
            stack.append(i)

        # previous smaller element
        pse = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                pse[stack.pop()] = i
            stack.append(i)

        # next greater element
        nge = [n] * n
        stack = []

        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                nge[index] = i
            stack.append(i)

        # previous greater element
        pge = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                pge[stack.pop()] = i
            stack.append(i)

        total = 0
        largest = 0
        smallest = 0

        for i in range(len(nums)):
            greater_left = i - pge[i]
            greater_right = nge[i] - i

            smaller_left = i - pse[i]
            smaller_right = nse[i] - i

            largest = largest + (greater_left * greater_right * nums[i])
            smallest = smallest + (smaller_left * smaller_right * nums[i])

        return largest - smallest
