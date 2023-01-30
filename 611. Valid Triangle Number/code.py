import bisect

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)-1):
                count = bisect.bisect_left(nums, nums[i] + nums[j], lo = j+1)
                res += count-j-1
        return res