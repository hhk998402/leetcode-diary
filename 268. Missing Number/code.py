class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        n = len(nums)
        expected_sum = n*(n+1)//2
        return expected_sum - sum1