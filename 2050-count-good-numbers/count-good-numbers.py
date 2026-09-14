class Solution:
    def countGoodNumbers(self, n: int) -> int:
        count = 0 
        prime = {2, 3, 5, 7}
        even = {2, 4, 6, 8}
        # def backtrack(i):
        #     if i == n:
        #         return 1
        #     tmp = 0
        #     if i%2 ==0:
        #         for ev in even:
        #             tmp += backtrack(i+1)
                
        #         return tmp
            
        #     if i%2 != 0 :
        #         for pr in prime:
        #             tmp+= backtrack(i+1)
                
        #         return tmp
        # return backtrack(0)
        MOD = 10**9 + 7
        if n % 2 == 0:
            position = n // 2
            return (pow(5, position, MOD) * pow(4, position, MOD)) % MOD
        else:
            even_pos = (n + 1) // 2
            odd_pos = n // 2
            return (pow(5, even_pos, MOD) * pow(4, odd_pos, MOD)) % MOD






        