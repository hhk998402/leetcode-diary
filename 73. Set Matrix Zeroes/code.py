class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        columns, rows = set(), set()
        m = len(matrix)
        n = len(matrix[0])
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == 0):
                    columns.add(j)
                    rows.add(i)
        for i in range(m):
            for j in range(n):
                if i in rows or j in columns:
                    matrix[i][j] = 0