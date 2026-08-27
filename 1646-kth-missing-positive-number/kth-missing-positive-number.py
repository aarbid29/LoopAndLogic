class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        alr = set(arr)
        count = 0

        for i in range(1, len(arr) + k + 1):
            if i in alr:
                continue

            count += 1

            if count == k:
                return i
