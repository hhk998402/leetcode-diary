class Solution:
    def mySqrt(self, x: int) -> int:
        #Find sqrt
        right = x//2
        left = 0
        if(x == 1):
            return 1
        elif(x == 0):
            return 0
        while(left+1 <= right):
            mid = (left + right)//2
            prod = mid*mid
            # print(left, right, mid)
            if(prod == x):
                return mid
            elif(prod > x):
                right = mid-1
            else:
                left = mid+1
        return right if right*right <= x else right-1
