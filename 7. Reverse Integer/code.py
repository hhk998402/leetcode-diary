class Solution:
    def reverse(self, x: int) -> int:
        reversedNum = 0
        digits = []
        mult = 10
        sign = -1 if x < 0 else 1
        x = x*-1 if x < 0 else x
        while(x):
            dig = x%10
            reversedNum = reversedNum*mult + dig 
            x = x//10
        reversedNum *= sign
        if(sign == -1):
            return reversedNum if reversedNum*(-1) <= 2**31 else 0
        else:
            return reversedNum if reversedNum <= (2**31)-1 else 0