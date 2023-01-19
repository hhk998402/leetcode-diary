import collections

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if(len(nums) < 2):
            return False
        s = 0
        res = 0
        d = collections.defaultdict(lambda: 0)
        d[0] = -1
        for idx,num in enumerate(nums):
            s = s + num
            rem = s%k
            if rem in d:
                if(idx - d[rem] > 1):
                    return True
            else:
                d[rem] = idx
        return False