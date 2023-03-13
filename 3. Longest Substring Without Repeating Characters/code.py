class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        res = 0
        maxLength = 0
        i = 0
        n = len(s)
        # print(s)
        while(i<n):
            # print(i)
            # if i == n-1:
            #     break
            if s[i] in d:
                i = d[s[i]] + 1
                d = {}
                d[s[i]] = i
                res = 1
            else:
                d[s[i]] = i
                res += 1
            if maxLength < res:
                maxLength = res
            i+=1
        return maxLength