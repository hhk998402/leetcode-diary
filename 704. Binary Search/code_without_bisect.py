import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo,hi = 0,n-1
        while(lo<=hi):
            mid = (lo+hi)//2
            if(nums[mid] == target):
                return mid
            elif(target < nums[mid]):
                hi = mid-1
            else:
                lo = mid+1
        return -1