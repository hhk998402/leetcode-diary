class Solution:
    graph = {}
    
    def addToQueue(self,i1,j1,i2,j2,mat):
        if(mat[i2][j2] == None or mat[i2][j2] > mat[i1][j1]):
            print((i1,j1), (i2,j2))
            mat[i2][j2] = mat[i1][j1] + 1
            return((mat,(i2,j2)))
        return(None)
            
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if(mat[i][j] == 0): #Add all zeroes to queue
                    queue.append((i,j))
                else: #In place replacement of non-zeroes with None
                    mat[i][j] = None
        while(queue):
            (i,j) = queue.popleft()
            if(i>0):
                res = self.addToQueue(i,j,i-1,j,mat)
                if(res != None):
                    mat = res[0]
                    queue.append(res[1])
            if(j>0):
                res = self.addToQueue(i,j,i,j-1,mat)
                if(res != None):
                    mat = res[0]
                    queue.append(res[1])
            if(j<n-1):
                res = self.addToQueue(i,j,i,j+1,mat)
                if(res != None):
                    mat = res[0]
                    queue.append(res[1])
            if(i<m-1):
                res = self.addToQueue(i,j,i+1,j,mat)
                if(res != None):
                    mat = res[0]
                    queue.append(res[1])
        return mat
                
                
                    