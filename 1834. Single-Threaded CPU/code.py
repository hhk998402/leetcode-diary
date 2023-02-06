import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_heap = []    
        heapq.heapify(task_heap)
        for i,task in enumerate(tasks):
            heapq.heappush(task_heap, (task[0], (task[1], i)))
        res = []
        time = task_heap[0][0]
        print(task_heap)
        queue = []
        heapq.heapify(queue)
        while(task_heap or queue):
            #Add all tasks that are within the time frame
            while(task_heap and task_heap[0][0] <= time):
                task = heapq.heappop(task_heap)
                heapq.heappush(queue, (task[1][0], task[1][1]))
            #Schedule next job
            if(queue):
                task = heapq.heappop(queue)
                time += task[0]
                res.append(task[1])
            elif(task_heap):
                time = task_heap[0][0]
        return res
