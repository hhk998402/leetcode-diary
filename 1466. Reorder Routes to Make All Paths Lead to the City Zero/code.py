class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        counter = 0
        (graph, bi_direc_graph) = self.formGraph(connections)
        queue = deque([0])
        visited = set()
        while(queue):
            ele = queue.popleft()
            if ele in visited:
                continue
            visited.add(ele)
            nodes = set(graph[ele]) - visited if ele in graph else set()
            counter += len(nodes)
            [queue.extend(graph[ele]) for x in nodes]
            [queue.append(x) for x in bi_direc_graph[ele]] if ele in bi_direc_graph else None
            # print(queue, ele, visited, counter)
        return counter
    
    def formGraph(self,connections):
        graph,bi_direc_graph = {},{}
        for connection in connections:
            fromVal = connection[0]
            toVal = connection[1]
            if(fromVal not in graph):
                graph[fromVal] = []
            if(toVal not in bi_direc_graph):
                bi_direc_graph[toVal] = []
            graph[fromVal].append(toVal)
            bi_direc_graph[toVal].append(fromVal)
        return (graph, bi_direc_graph)