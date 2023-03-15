class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Sort by the end time in the intervals
        intervals.sort(key = lambda x : x[1])
        endVal = intervals[0][1]
        cnt = 1
        for i in range(1,len(intervals)):
            if endVal <= intervals[i][0]:
                cnt += 1
                endVal = intervals[i][1]
            else:
                #Discard the interval
                continue
        return len(intervals) - cnt