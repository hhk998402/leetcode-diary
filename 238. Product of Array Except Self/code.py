class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for x in range(len(nums))]
        ptr1 = 1
        ptr2 = 1
        for i in range(1,len(nums)):
            ptr1 *= nums[i-1]
            res[i] *= ptr1
            ptr2 *= nums[len(nums) - i]
            res[len(nums) - i - 1] *= ptr2
        return(res)