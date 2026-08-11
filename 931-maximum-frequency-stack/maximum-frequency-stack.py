
class FreqStack:

    def __init__(self):
        self.heap = []
        self.mp = defaultdict(int)
        self.order = 0

    def push(self, val: int) -> None:
        self.mp[val] += 1
        self.order += 1

        # (-frequency, -order, value)
        heapq.heappush(
            self.heap,
            (-self.mp[val], -self.order, val)
        )

    def pop(self) -> int:
        freq, order, val = heapq.heappop(self.heap)

        self.mp[val] -= 1

        return val