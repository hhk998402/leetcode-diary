from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        d1,d2 = defaultdict(lambda:0),defaultdict(lambda:0)
        if(n1 != n2):
            return False
        for i in range(n1):
            d1[s[i]] += 1
            d2[t[i]] += 1
        if(len(d1.keys()) != len(d2.keys())):
            return False
        for k in d1.keys():
            if k not in d2:
                return False
            if d1[k] != d2[k]:
                return False
        return True
            
        