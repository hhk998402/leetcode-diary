class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        leftPtr = 0
        n = len(s)
        freq = {}
        longestStr = 0
        for rightPtr in range(n):
            if s[rightPtr] not in freq:
                freq[s[rightPtr]] = 0
            freq[s[rightPtr]] += 1

            #Condition for changing longestStr
            cnt = rightPtr - leftPtr + 1
            if(cnt - max(freq.values()) <= k):
                longestStr = max(longestStr, cnt)
            else:
                freq[s[leftPtr]] -= 1
                #Pop out the character from freq dict if all occurences run out
                if not freq[s[leftPtr]]:
                    freq.pop(s[leftPtr])
                leftPtr += 1
        return longestStr