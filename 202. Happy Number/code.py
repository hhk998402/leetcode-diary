class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True

        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.calc(n)

        return n==1
            
    def calc(self, n):
        sum1 = 0
        while(n):
            sum1 += (n%10)**2
            n = n//10
        return sum1
        