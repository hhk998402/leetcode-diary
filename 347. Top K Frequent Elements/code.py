import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        d = collections.defaultdict(lambda: 0)
        for num in nums:
            d[num] += 1

        res = []
        for i in range(n,0,-1):
            if i in d.values():
                vals = [j for j in d if d[j] == i]
                for v in vals:
                    res.append(v)
                    k-=1
                    if k == 0:
                        break
            if k == 0:
                break
        return res