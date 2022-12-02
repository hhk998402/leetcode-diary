class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        chk,k = 0,0
        n = len(s)
        vowels = set(['a','e','i','o','u'])
        for letter in s.lower():
            if(letter in vowels):
                if(n//2 <= k):
                    chk -= 1
                else:
                    chk += 1
            k+=1
        return chk == 0