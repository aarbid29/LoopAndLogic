class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        i = 0 
        j = 0 
        flip = 0
        while i < len(s) and j <len(goal):
            if s[i]!= goal[j]:
                flip+=1
            i+=1
            j+=1
        
        if flip >2:
            return False
        if flip ==1 :
            return False
        
        if flip == 0:
            return max(Counter(s).values())>=2
        
        return Counter(s)==Counter(goal)
        



            




        