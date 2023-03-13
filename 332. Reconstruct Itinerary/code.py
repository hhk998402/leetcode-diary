import bisect

class Node:
    def __init__(self, val):
        self.val = val
        self.connections = []                

    def setConnection(self,dest):
        bisect.insort_left(self.connections, (dest,False))

class Solution:
    def __init__(self):
        self.path = []
        self.starts = {}

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        for i,j in tickets:
            if i not in self.starts:
                self.starts[i] = Node(i)
            self.starts[i].setConnection(j)
        self.dfs("JFK",0,n)
        return(self.path)
        
    def dfs(self, node, curSteps, target):
        self.path.append(node)
        if curSteps == target:
            return True
        if node in self.starts:
            for idx,(nodeVal,visited) in enumerate(self.starts[node].connections):
                if not visited:
                    self.starts[node].connections[idx] = (nodeVal,True)
                    res = self.dfs(nodeVal,curSteps+1,target)
                    if res:
                        return True
                    else:
                        self.starts[node].connections[idx] = (nodeVal,False)
                        self.path = self.path[:max(1,curSteps+1)]
        return False
            