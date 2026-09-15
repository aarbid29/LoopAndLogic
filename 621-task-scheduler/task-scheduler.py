class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [] #heap to keep track of which task to execute
        freq = Counter(tasks)
        for key,value in freq.items():
            heapq.heappush(heap,(-value,key))
        global_time= 0 
        dq = deque() #to keep unavailable tasks somewhere else cooldown ends
        #initally every unique tasks are  available
        #heap (-frequency, task)
        # dq (available_time, frequency, task)

        while heap or dq:
            global_time+=1
            if not heap:
                global_time = dq[0][0]
            
            while dq  and dq[0][0]<= global_time:
                time,freq,task = dq.popleft()
                heapq.heappush(heap,(freq,task))
            
            freq , task = heapq.heappop(heap)
            rem = freq+1
            if rem == 0:
                continue
            dq.append((global_time+n+1,rem,task))
        
        return global_time













 

    






        