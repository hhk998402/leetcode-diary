class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin, curMax = prices[0], 0
        minIdx, maxIdx = 0,0
        maxProfit = 0
        for i in range(1,len(prices)):
            val = prices[i]
            if curMin > val:
                curMin = val
                minIdx = i
                if(minIdx > maxIdx):
                    curMax = prices[i]
                    maxIdx = i
            if curMax < val:
                curMax = val
                maxIdx = i
            curProfit = curMax - curMin if minIdx<maxIdx else 0
            if(curProfit > maxProfit):
                maxProfit = curProfit
        return maxProfit