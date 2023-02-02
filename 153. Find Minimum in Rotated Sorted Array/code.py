class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        lo = 0
        n = len(nums)
        hi = n-1
       
        while(lo<hi):
            mid = (lo+hi)//2
            # print(lo,hi,mid,nums[mid])
            if(nums[lo] < nums[hi]):
                return nums[lo]
            if(lo + 1 == hi):
                return nums[hi]
            elif(nums[lo] < nums[mid] and nums[hi] < nums[mid]):
                lo = mid+1
            else:
                hi = mid
        return nums[lo]