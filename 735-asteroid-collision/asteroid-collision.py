class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for stone in asteroids:
            # Right-moving asteroid hits left-moving asteroid
            while stack and (stack[-1] > 0 and stone < 0):

                summ = stack[-1] + stone

                if summ>0:
                    stone = 0 
                
                if summ<0:
                    stack.pop()


                if summ ==0:
                    stack.pop()
                    stone = 0 

            if stone != 0:
                stack.append(stone)
        return stack





        