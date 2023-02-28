class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        prevNumber = None
        for i in range(numRows):
            row = []
            if(i == 0):
                row.append(1)
            elif(i == 1):
                row.append(1)
                row.append(1)
                prevNumber = "11"
            else:
                row.append(1)
                prevDig = prevNumber[0]
                print(prevNumber)
                for i in range(1,len(prevNumber)):
                    row.append(prevDig + prevNumber[i])
                    prevDig = prevNumber[i]
                row.append(1)
            prevNumber = row
            res.append(row)
        return(res)