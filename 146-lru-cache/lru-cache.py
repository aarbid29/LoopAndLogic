from collections import defaultdict

class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.count = 0
        self.time = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1

        self.time += 1
        self.mp[key][0] = self.time

        return self.mp[key][1]

    def put(self, key: int, value: int) -> None:
        self.time += 1
        if key in self.mp:
            self.mp[key][0] = self.time
            self.mp[key][1] = value
            return

        if self.count >= self.capacity:
            least = min(self.mp, key=lambda k: self.mp[k][0])
            del self.mp[least]
            self.count -= 1

        self.mp[key] = [self.time, value]
        self.count += 1