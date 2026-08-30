class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minn = min(nums)
        ind1 = nums.index(minn)

        maxx = max(nums)
        ind2 = nums.index(maxx)

        n = len(nums)

        def simulate(first, second):
            used = [False] * n
            operations = 0

            if first[1] == "front":
                i = 0
                while i <= first[0]:
                    if not used[i]:
                        operations += 1
                        used[i] = True
                    i += 1
            else:
                i = n - 1
                while i >= first[0]:
                    if not used[i]:
                        operations += 1
                        used[i] = True
                    i -= 1

            if second[1] == "front":
                i = 0
                while i <= second[0]:
                    if not used[i]:
                        operations += 1
                        used[i] = True
                    i += 1
            else:
                i = n - 1
                while i >= second[0]:
                    if not used[i]:
                        operations += 1
                        used[i] = True
                    i -= 1

            return operations

        ans = min(
            simulate((ind1, "front"), (ind2, "front")),
            simulate((ind1, "back"), (ind2, "back")),
            simulate((ind1, "front"), (ind2, "back")),
            simulate((ind1, "back"), (ind2, "front"))
        )

        return ans
