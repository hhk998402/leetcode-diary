import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        for i in range(0,len(nums)-k):
            heapq.heappop(nums)
        self.nums = nums
        self.k = k
        print(self.nums)

    def add(self, val: int) -> int:
        kthLargest = heapq.heappop(self.nums) if len(self.nums) == self.k else float("-inf")
        res = None
        # print(kthLargest, self.nums, val)
        if(val > kthLargest or len(self.nums) < self.k - 1):
            # print("Here")
            heapq.heappush(self.nums, val)
            res = heapq.heappop(self.nums)
            heapq.heappush(self.nums, res)
            if(len(self.nums) < self.k):
                heapq.heappush(self.nums, kthLargest)
            # print(self.nums)
        else:
            heapq.heappush(self.nums, kthLargest)
            res = kthLargest
        return res


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)