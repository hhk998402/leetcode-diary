class Solution:

    def __init__(self):
        self.dfsId = {}
        self.oldestReachableId = {}
        self.criticalEdges = []
        self.timestamp = 0

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for x in range(n)]
        #Construct adjacency matrix
        for i,ele in enumerate(connections):
            a,b = ele[0],ele[1]
            adj[a].append(b)
            adj[b].append(a)
        #To deal with [[0,1]] case
        if(len(connections) == 1):
            return connections
        self.findCriticalEdges(adj,0,None)
        return self.criticalEdges
    
    def findCriticalEdges(self, adj, currNode, parentNode):
        self.timestamp += 1
        self.oldestReachableId[currNode] = self.timestamp
        self.dfsId[currNode] = self.timestamp
        
        
        for neighbor in adj[currNode]:
            #Prevent cyclical checking
            if(parentNode == neighbor):
                continue

            if(neighbor not in self.dfsId):
                self.findCriticalEdges(adj, neighbor, currNode)
            
            self.oldestReachableId[currNode] = min(self.oldestReachableId[neighbor], self.oldestReachableId[currNode])
            if(self.oldestReachableId[neighbor] > self.dfsId[currNode]):
                self.criticalEdges.append([currNode,neighbor])
