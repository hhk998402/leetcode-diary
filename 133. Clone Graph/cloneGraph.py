"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import *

class Solution:
    d = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.traverseGraph(node)
    
    def traverseGraph(self, node):
        if(not node):
            return None
        if(node in self.d):
            return self.d[node]
        
        #Attempt to create new node
        newNode = Node(node.val, [])
        self.d[node] = newNode
        #Traverse recursively through neighbors
        for neighbor in node.neighbors:
            self.d[node].neighbors.append(self.traverseGraph(neighbor))
        return newNode