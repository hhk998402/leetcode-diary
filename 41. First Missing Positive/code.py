import heapq

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [num for num in nums if num > 0]
        heapq.heapify(nums)
        res = None
        if(len(nums) == 0 or (len(nums) >= 0 and nums[0] != 1)):
            return 1
        else:
            prevNumber = heapq.heappop(nums)
            currNumber = None
            if len(nums) != 0:
                currNumber = heapq.heappop(nums)
            while(currNumber and not res):
                if(currNumber > prevNumber + 1):
                    res = prevNumber + 1
                else:
                    prevNumber = currNumber
                    if len(nums) == 0:
                        currNumber = None
                    else:
                        currNumber = heapq.heappop(nums)
            if res == None:
                res = prevNumber + 1
        return res
        