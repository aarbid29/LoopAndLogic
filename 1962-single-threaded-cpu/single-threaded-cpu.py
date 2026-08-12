class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(en, pr, i) for i, (en, pr) in enumerate(tasks)]
        tasks.sort()
    
        heap = []
        time = tasks[0][0]
        res = []
        i = 0

        while i < len(tasks) or heap:

            while i < len(tasks) and tasks[i][0] <= time:
                en, pr, idx = tasks[i]
                heapq.heappush(heap, (pr, idx))
                i += 1
            # if no available task, jump time forward
            if not heap:
                time = tasks[i][0]
                continue



            pr, idx = heapq.heappop(heap)
            res.append(idx)
            time += pr

        return res

            



             

                
            





        