class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0]!=5:
            return False
        summ = 0
        five = 0
        ten = 0
        for dollar in bills:

            if dollar ==5:
                five+=5
            
            elif dollar ==10:
                if five>=5:
                    five-=5
                    ten+=10
                else:
                    return False 
            else:
                if ten>=10 and five>=5:
                    ten-=10
                    five-=5
                elif five>=15:
                    five-=15
                else:
                    return False
        return True
            



