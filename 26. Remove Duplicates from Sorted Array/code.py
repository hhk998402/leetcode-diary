class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prevNumber = nums[0]
        idx = 0
        for i in range(1,len(nums)):
            if(nums[i] != prevNumber):
                idx+=1
                nums[idx] = nums[i]
                prevNumber = nums[i]
        return idx+1