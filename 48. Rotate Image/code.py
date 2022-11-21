class Solution:
    def swapElements(self, idx1, idx2, mat):
        temp = mat[idx1[0]][idx1[1]]
        mat[idx1[0]][idx1[1]] = mat[idx2[0]][idx2[1]]
        mat[idx2[0]][idx2[1]] = temp
        print("Matrix", mat)
        return mat
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #1. Perform transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix = self.swapElements((i,j),(j,i),matrix)
        #2. Reverse elements in each row
        for i in range(n):
            matrix[i].reverse()
