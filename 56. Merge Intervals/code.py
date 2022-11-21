class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        idx = 0
        res = []
        for i,ele in enumerate(intervals):
            if(len(res) == 0):
                res.append(ele)
                continue
            if(res[idx][1] >= ele[0]):
                res[idx][1] = max(ele[1],res[idx][1])
            else:
                idx += 1
                res.append(ele)
        return res