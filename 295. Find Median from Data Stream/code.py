class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        idx = self.findIdx(0,len(self.arr)-1,num)
        n = len(self.arr)
        if(n == 0):
            self.arr.append(num)
        else:
            # self.arr = self.arr[:idx] + [num] + self.arr[idx:]
            # print("Number is num", num, idx, self.arr)
            if(n <= idx):
                self.arr.append(num)
            else:
                self.arr.insert(idx,num)
        # print(self.arr, idx)
        
    def findIdx(self,min1,max1,num):
        if(len(self.arr) == 0):
            return 0
        while(min1 <= max1):
            mid = (min1+max1)//2
            if(self.arr[mid] == num):
                return mid
            elif(self.arr[mid] < num):
                min1 = mid + 1
            else:
                max1 = mid - 1
        return max1 + 1



    def findMedian(self) -> float:
        n = len(self.arr)
        if(n == 2):
            return sum(self.arr)/2.0
        if(n%2 == 0):
            # print("Inside even median", n, n//2, (n//2)+1, self.arr)                
            return (self.arr[(n-1)//2] + self.arr[((n-1)//2)+1])/2.0
        else:
            return self.arr[n//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()