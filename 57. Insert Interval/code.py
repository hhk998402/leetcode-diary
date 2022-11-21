class Solution:
    def findPosToInsert(self,arr,ele):
        min1 = 0
        max1 = len(arr)-1
        while(min1<=max1):
            mid = (min1+max1)//2
            if(arr[mid][0] == ele[0]):
                return mid
            elif(arr[mid][0] < ele[0]):
                min1 = mid + 1
            else:
                max1 = mid - 1
        return max1 + 1

    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        idx = self.findPosToInsert(intervals,newInterval)
        intervals.insert(idx, newInterval)
        print(idx, intervals, newInterval)
        res = intervals[:idx]
        # count = 0
        for i,ele in enumerate(intervals[idx:]):
            # print("Index ", idx, res, ele, res[idx-1][1], ele[0])
            # count+=1
            if(len(res) == 0):
                res.append(ele)
                continue
            if(res[idx-1][1] >= ele[0]):
                # print("here", res[idx-1][1], ele[0])
                res[idx-1][1] = max([ele[1], res[idx-1][1]])
            else:
                idx += 1
                res.append(ele)
        # res += intervals[idx+count:]
        return res