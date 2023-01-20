from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        islands = 0
        directions = [[-1,0], [0,-1], [1,0], [0,1]]
        for i in range(m):
            for j in range(n):
                if (i,j) in visited or grid[i][j] == "0":
                    continue

                q = deque([])
                q.append(tuple([i,j]))
                chk = True
                while(q):
                    x,y = q.popleft()
                    if((x,y) in visited):
                        continue
                    visited.add((x,y))
                    chk = True
                    for [_x, _y] in directions:
                        x1 = x+_x
                        y1 = y+_y
                        if((x1,y1) not in visited and x1 < m and x1 >= 0 and y1 < n and y1 >= 0 and grid[x1][y1] == "1"):
                            q.append((x1,y1))
                if(chk):
                    islands += 1
        return islands
                    