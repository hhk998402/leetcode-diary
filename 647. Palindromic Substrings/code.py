class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countSubstringAroundLetter(i,i,s) + self.countSubstringAroundLetter(i,i+1,s)
        return res

    def countSubstringAroundLetter(self, left, right, s):
        n = len(s)
        cnt = 0
        while(left >= 0 and right < n and s[left] == s[right]):
            left -= 1
            right += 1
            cnt += 1
        return cnt