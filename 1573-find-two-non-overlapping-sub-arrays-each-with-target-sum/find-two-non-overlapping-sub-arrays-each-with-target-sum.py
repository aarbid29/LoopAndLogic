class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float("inf")

        l = 0 
        running_sum = 0
        best = [INF] * n
        ans = INF

        for r in range(n):
            running_sum+= arr[r]

            while running_sum > target:
                left = arr[l]
                running_sum-=left
                l+=1
            
            if running_sum == target:
                length = r-l+1
                if l > 0 and best[l - 1] != INF:
                    best_min_leftof_l = best[l-1]
                    ans = min(ans, length+ best_min_leftof_l)

                best[r] = min(best[r - 1], length)


            else:
                if r>0: #to skip r-1 -ve index
                    best[r] = best[r-1]
        
        return -1 if ans == INF else ans

        

