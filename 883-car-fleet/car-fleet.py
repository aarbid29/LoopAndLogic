class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)
        fleet = 0
        stack = []

        for position,speed in cars:

            time = (target - position) / speed

            if  not stack or time > stack[-1]:
                stack.append(time)
                fleet+=1

        
        return fleet





        
        