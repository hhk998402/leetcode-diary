import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Find separation/pivot point
        n = len(nums)
        i,j = 0,n-1
        breakpt = 0
        while(i<j):
            if(i+1<n and j-1 >= 0):
                if(nums[i] > nums[i+1]):
                    breakpt = i+1
                    break
                elif(nums[j] < nums[j-1]):
                    breakpt = j
                    break
            else:
                breakpt = 0
                break
            i+=1
            j-=1
        #Do normal bisect on pieces of array
        idx1, idx2 = bisect.bisect_left(nums, target, lo=0, hi=breakpt), bisect.bisect_left(nums, target, lo=breakpt, hi=n)
        # print(idx1, idx2, nums, target)
        if idx1 != n and nums[idx1] == target:
            return idx1
        elif idx2 != n and nums[idx2] == target:
            return idx2
        else:
            return -1
