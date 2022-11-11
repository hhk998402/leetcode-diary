from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict = {}
        res = []
        idx = 0
        for num in nums:
            key = target - num
            if(num in sumDict):
                res.append(sumDict[num])
                res.append(idx)
                break
            else:
                sumDict[key] = idx
            idx += 1
        return res

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))