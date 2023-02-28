class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        # if(len(s) == 1 and s[0] in wordSet):
        #     return True

        self.loc = [[] for i in range(len(s))]
        wordBreakPossible = False
        n = len(s)
        self.visited = set()
        firstLetter = True
        self.candidates = 0
        idx = 0
        while(not wordBreakPossible and idx < n and (firstLetter or len(self.visited) <= self.candidates)):
            if firstLetter:
                wordBreakPossible = self.dfs(idx, wordSet, s)
                firstLetter = False
            else:
                for l in self.loc[idx]:
                    if((idx, l) in self.visited):
                        continue
                    else:
                        self.visited.add((idx,l))
                        wordBreakPossible = self.dfs(l, wordSet, s)
                        if(wordBreakPossible):
                            break
                idx += 1
                # print(self.loc, idx, wordBreakPossible, self.visited, self.candidates)
        return wordBreakPossible


    def dfs(self, idx, wordSet, s):
        if(idx >= len(s)):
            return True
        ch = s[idx]
        currWord = ch
        if currWord in wordSet:
            self.loc[idx].append(idx+1)
            self.candidates += 1
        for i in range(idx+1, len(s)):
            currWord += s[i]
            if(currWord in wordSet):
                self.loc[idx].append(i+1)
                self.candidates += 1
                if(i+1 >= len(s)):
                    #Reached last letter of string
                    return True
        return False
                  