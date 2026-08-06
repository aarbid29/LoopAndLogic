class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gas = gas + gas
        cost = cost + cost
        tank = 0
        s_index = -1
        chosen = True
        count = 0
        for i in range(len(gas)):
            if count == n:
                return s_index % n
            if tank + gas[i] < cost[i]:
                s_index = i + 1
                chosen = False
                tank = 0
                count = 0
                continue
            count += 1
            if chosen:
                s_index = i
                chosen = False
            tank += gas[i]
            tank -= cost[i]

        return -1