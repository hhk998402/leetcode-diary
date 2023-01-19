class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            word1 = ''.join(sorted(word))
            if word1 not in d:
                d[word1] = []
            d[word1].append(word)
        return d.values()
