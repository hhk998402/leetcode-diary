class Solution:
    def rob(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        maxRob = 0
        for i in range(n-1,-1,-1):
            s1 = set(range(i+2,n))
            curMax = nums[i]
            maxSum = 0
            print(s1,i)
            for j in s1:
                if(d[j]>maxSum):
                    maxSum = d[j]
            d[i] = curMax + maxSum
            if(d[i] > maxRob):
                maxRob = d[i]
        print(d)
        return maxRob