class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i,ele in enumerate(nums):
            #Duplicate checking logic for i
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j = i+1
            k = len(nums) - 1
            while(j<k):
                sum1 = nums[i] + nums[j] + nums[k]
                if(sum1 == 0):
                    res.append((nums[i], nums[j], nums[k]))
                    j+=1
                    #Duplicate checking logic for j
                    while(j < k and nums[j] == nums[j-1]):
                        j+=1
                elif(sum1 < 0):
                    j+=1
                else:
                    k-=1
        # return res
        return list(set(res))

#Time Complexity = O(nlogn + n^2) = O(n^2)