class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                res = self.dfs(board, word, 0, i, j, m, n)
                if res:
                    return True
        return False
    
    def dfs(self, board, word, idx, i, j, m, n):
        pos = [[-1,0],[0,-1],[1,0],[0,1]]
        if board[i][j] != word[idx]:
            return False #backtrack
        
        idx += 1

        if idx == len(word):
            return True
        
        temp = board[i][j]
        board[i][j] = "#"

        for _x,_y in pos:
            x1,y1 = i+_x, j+_y
            if(x1 >= 0 and x1 < m and y1 >= 0 and y1 < n and board[x1][y1] != "#"):
                res = self.dfs(board, word, idx, x1, y1, m, n)
                if res:
                    return True

        board[i][j] = temp

        return False
