from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda: 0)
        d[0] = 1
        psum = 0
        res = 0
        for num in nums:
            psum += num
            res += d[psum%k]
            d[psum%k] += 1
        return res