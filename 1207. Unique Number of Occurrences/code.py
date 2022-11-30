class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        freq = set()
        chk, curNum = 0,None
        for i in arr:
            if(not curNum):
                curNum = i
            if(i == curNum):
                chk+=1
            else:
                if(chk not in freq):
                    freq.add(chk)
                    curNum = i
                    chk = 1
                else:
                    return False
        return chk not in freq