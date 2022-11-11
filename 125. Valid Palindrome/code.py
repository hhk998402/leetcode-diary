class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPtr = 0
        rightPtr = len(s)-1
        while(leftPtr <= rightPtr):
            if(not s[leftPtr].isalnum()):
                leftPtr += 1
                continue
            if(not s[rightPtr].isalnum()):
                rightPtr -= 1
                continue
            if(s[leftPtr].lower() != s[rightPtr].lower()):
                return False
            leftPtr += 1
            rightPtr -= 1
        return True