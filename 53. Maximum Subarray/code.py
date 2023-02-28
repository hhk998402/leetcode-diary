class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        curSum = 0
        maxSumModified = False
        for i in nums:
            if(curSum + i < 0):
                curSum = 0
                continue
            curSum += i
            if maxSum < curSum:
                maxSumModified = True
                maxSum = curSum
        return maxSum if maxSumModified else max(nums)