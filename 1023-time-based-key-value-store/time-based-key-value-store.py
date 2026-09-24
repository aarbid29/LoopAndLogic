class TimeMap:
    def __init__(self):
        self.name = defaultdict(list)
        self.timeval = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.name[key].append(timestamp)
        self.timeval[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        arr = self.name[key]
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if arr[mid] == timestamp:
                return self.timeval[key][timestamp]

            elif arr[mid] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        if r < 0:
            return ""
        return self.timeval[key][arr[r]]