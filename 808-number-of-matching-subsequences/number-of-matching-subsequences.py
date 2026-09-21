class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        count = 0
        mp =defaultdict(list)
        for i,char in enumerate(s):
            mp[char].append(i)

        def check(s, words):
            cursor = -1
            for word in words:
                arr = mp[word]
                index = bisect_left(arr,cursor)

                if index == len(arr):
                    return False
                
                cursor = arr[index]+1

            return True
        for word in words:
            if check(s,word):
                count+=1
        return count


        