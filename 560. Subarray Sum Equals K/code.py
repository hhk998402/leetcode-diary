from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda: 0)
        d[0] = 1
        ans, sum1 = 0,0
        for n in nums:
            sum1 += n
            ans += d[sum1-k]
            d[sum1] += 1
        return ans