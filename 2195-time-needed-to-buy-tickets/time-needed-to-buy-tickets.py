class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        dq = deque((tickets[i], i) for i in range(len(tickets)))
        time = 0

        while dq:
            val, index = dq.popleft()
            time += 1

            if index == k and val == 1:
                return time

            if val > 1:
                dq.append((val - 1, index))

        return time

