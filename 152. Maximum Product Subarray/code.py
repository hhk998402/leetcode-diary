class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Forward pass
        maxProd = float('-inf')
        curProd = None
        for i in range(len(nums)):
            if nums[i] == 0:
                if curProd and maxProd < curProd:
                    maxProd = curProd
                curProd = None
                continue
            if not curProd:
                curProd = 1
            curProd *= nums[i]
            if(maxProd < curProd):
                maxProd = curProd
        print(maxProd)
        #Backward pass
        backMaxProd = float('-inf')
        curProd = None
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                if curProd and backMaxProd < curProd:
                    backMaxProd = curProd
                curProd = None
                continue
            if not curProd:
                curProd = 1
            curProd *= nums[i]
            if(backMaxProd < curProd):
                backMaxProd = curProd
        print(backMaxProd)
        return 0 if backMaxProd <= 0 and maxProd <= 0 and 0 in nums else max(backMaxProd, maxProd)