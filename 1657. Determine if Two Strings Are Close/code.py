import collections

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)
        if n1 != n2:
            return False
        set1 = set(word1)
        set2 = set(word2)
        if set1 != set2:
            return False
        d1, d2 = {}, {}
        for letter in word1:
            if(letter not in d1):
                d1[letter] = 0
            d1[letter] += 1
        for letter in word2:
            if(letter not in d2):
                d2[letter] = 0
            d2[letter] += 1
        # return sorted(d2.values()) == sorted(d1.values())
        compare = lambda x,y : collections.Counter(x) == collections.Counter(y)
        return compare(d2.values(), d1.values())
        