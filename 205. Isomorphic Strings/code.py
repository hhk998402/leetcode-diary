class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        count = 1
        str1 = ""
        for ch in s:
            if ch not in d:
                d[ch] = str(count)
                count += 1
            str1 += d[ch]
        d = {}
        count = 1
        str2 = ""
        for ch in t:
            if ch not in d:
                d[ch] = str(count)
                count += 1
            str2 += d[ch]
        return str1 == str2