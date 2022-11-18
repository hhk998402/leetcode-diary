class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sortedList = sorted(nums)
        res = 0
        for i in range(0,len(sortedList),2):
            res += sortedList[i]
        return res