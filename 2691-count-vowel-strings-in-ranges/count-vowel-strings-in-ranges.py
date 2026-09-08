class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = "aeiou"
        arr = [0]* len(words)
        for i, char in enumerate(words):
            if char[0] in vowels and char[-1] in vowels:
                arr[i]=1
        #total sum till a ___ index
        mp = defaultdict(int)
        running_sum = 0 
        for index , digit in enumerate(arr):
            running_sum+=digit
            mp[index] = running_sum
            
        res = []
        for i,j in queries:
            res.append(mp[j]-mp[i-1])

        return res




        


        

        

        



        