class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        res = [] 

        line = 0 
        runningsum = 0 

        for char in s:
            asci = ord(char) -ord("a")
            value = widths[asci]

            if runningsum+ value >100:
                line+=1
                runningsum = 0
            
            runningsum+=value
        
        if runningsum >0:
            line+=1
            
        res.append(line)
        res.append(runningsum)
        return res
        

        