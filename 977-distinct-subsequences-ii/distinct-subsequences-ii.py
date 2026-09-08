class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mp = defaultdict(int)
        total= 0 
        MOD = 10**9+7

        for i in range(len(s)):
            char = s[i]
            old_total = total

            # possible_subsequence = pow(2, i, MOD)

            if char not in mp:
                new_subseq = (old_total + 1) % MOD
                mp[char] = new_subseq
                total += new_subseq
            
            else:
                new_subseq = (old_total + 1 - mp[char]) % MOD
                mp[char]+= new_subseq
                total+= new_subseq

        return total % MOD
