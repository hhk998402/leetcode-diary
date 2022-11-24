class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(numbers)-1
        while(ptr1<ptr2):
            a = numbers[ptr1]
            b = numbers[ptr2]
            sum1 = a+b
            if(sum1 == target):
                return [ptr1+1,ptr2+1]
            elif(sum1 < target):
                ptr1+=1
            else:
                ptr2-=1
        