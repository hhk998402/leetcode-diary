import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*x for x in stones]
        heapq.heapify(stones)
        while(len(stones) > 1):
            val1 = -heapq.heappop(stones)
            val2 = -heapq.heappop(stones)
            res = 0
            if val1 != val2:
                res = val1 - val2
            heapq.heappush(stones, -res)
        return(-heapq.heappop(stones))