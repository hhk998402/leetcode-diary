from collections import defaultdict, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        timestamp = 0
        task_time_mapping = defaultdict(lambda: float("-inf"))
        freq = Counter(tasks)
        task_freq = []
        for k,v in freq.items():
            task_freq.append((-v,k))
        heapq.heapify(task_freq)
        queue = []
        # print(task_freq)
        while(queue or task_freq):
            timestamp += 1
            # print("Task Freq", task_freq)
            if task_freq:
                task_data = heapq.heappop(task_freq)
                freq1, task = -task_data[0], task_data[1]
                freq1 -= 1
                if freq1 > 0: # We need to let it cooldown
                    queue.append((freq1,task,timestamp))
            #Clear the queue wherever possible and place back into heap
            temp_queue = queue
            for idx,val in enumerate(queue):
                if timestamp >= val[2] + n:
                    del temp_queue[idx]
                    heapq.heappush(task_freq, (-val[0], val[1]))
            queue = temp_queue
            # print(temp_queue)
            # break
        return(timestamp)