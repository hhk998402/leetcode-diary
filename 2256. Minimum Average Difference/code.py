class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        runningSum = 0
        minDiff, idx = float('inf'), 0
        n,runningCount = len(nums),0
        for num in nums:
            runningCount += 1
            runningSum += num
            remainingSum = totalSum - runningSum
            diff = abs((runningSum//runningCount - remainingSum // (n-runningCount))) if runningCount < n else abs(runningSum//runningCount)
            if(minDiff > diff):
                minDiff = diff
                idx = runningCount - 1
        return idx
        