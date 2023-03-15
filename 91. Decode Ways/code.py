class Solution:
    def numDecodings(self, s: str) -> int:
        res = self.dfs(0,0,s) + self.dfs(0,1,s)
        return(res)

    @lru_cache(maxsize=None)
    def dfs(self, idx, digInc, s):
        if idx + digInc >= len(s):
            return 0
        seq = s[idx:idx+digInc+1]
        if seq[0] == "0":
            return 0
        ch = int(seq) + 64
        if ch >= 65 and ch <= 90:
            if idx+digInc == len(s)-1:
                return 1
            else:
                return self.dfs(idx+digInc+1, 0, s) + self.dfs(idx+digInc+1, 1, s)
        return 0 