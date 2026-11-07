class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        heap = []
        busy = []
        res = []
        globaltime = 0

        for i, server in enumerate(servers):
            heapq.heappush(heap, (server, i))

        for i, task in enumerate(tasks):
            globaltime = max(globaltime, i)

            while heap or busy:
                if not heap:
                    globaltime = busy[0][0]

                while busy and busy[0][0] <= globaltime:
                    taken, pc, idd = heapq.heappop(busy)
                    heapq.heappush(heap, (pc, idd))

                if heap:
                    cpu, idx = heapq.heappop(heap)
                    res.append(idx)

                    new_time = globaltime + task
                    heapq.heappush(busy, (new_time, cpu, idx))
                    break

        return res