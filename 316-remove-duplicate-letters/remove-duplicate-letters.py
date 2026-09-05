class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        freq = Counter(s)
        stack = []
        seen = set()

        for i in range(len(s)):
            char = s[i]
            freq[char]-=1        
            if char in seen:
                continue 
            while stack and stack[-1]> char and freq[stack[-1]]>0:
                seen.remove(stack[-1])
                stack.pop()

            stack.append(char)
            seen.add(char)
        
        return "".join(stack)
        