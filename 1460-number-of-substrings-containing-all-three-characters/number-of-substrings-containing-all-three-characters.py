class Solution:
    def numberOfSubstrings(self, s: str) -> int:


        mp =defaultdict(int)
        #if freq of all char is 1 , how many substring can be created
        #with the value ending at nums[r] in sliding window
        l =0
        count = 0
        old_mp = defaultdict(int)
        for r in range(len(s)):

            mp[s[r]]+=1

            #then the window has len of 3 , ie has all character
            #need to find the first occurance where it all has 3 characters
            while len(mp)>=3:
                left = s[l]
                mp[left]-=1
                if mp[left]==0:
                    del mp[left]
                l+=1
            count+=l

        return count
                

            




