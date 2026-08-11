class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7

        nse = [n] * n
        stack = []

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                index = stack.pop()
                nse[index] = i

            stack.append(i)

        pse = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                pse[stack.pop()] = i
            stack.append(i)

        total = 0

        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i

            count = left * right

            contribution = arr[i] * count

            total = (total + contribution) % MOD

        return total