class Node:
    def __init__(self):
        self.connections = {}
        self.word = ""
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insertWord(self, word):
        node = self.root
        for letter in word:
            child = Node()
            if(letter not in node.connections):
                node.connections[letter] = child
            child = node.connections[letter]
            node = child
        node.is_word = True
        node.word = word

class Solution:
    m = 0
    n = 0

    def __init__(self):
        self.m, self.n = 0,0

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if(not board):
            return []

        trie = Trie()
        for word in words:
            trie.insertWord(word)

        #Traverse through board, and mark out the found words while doing so
        results = set()
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                visited = set()
                visited.add((i,j))
                self.search_board(results,board,visited,i,j,trie.root.connections.get(board[i][j]))
                if(len(results) >= len(words)):
                    break

        return list(set(results))
    
    def search_board(self,results,board,visited,i,j,node):
        # print(i,j, visited)
        if not node:
            return
        if node.is_word:
            results.add(node.word)
        
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for i1,j1 in directions:
            i2 = i+i1
            j2 = j+j1
            if i2 >= 0 and i2 < self.m and j2 >= 0 and j2 < self.n and (i2,j2) not in visited:
                visited.add((i2,j2))
                # print("i2 = ",i2,"j2 = ",j2, visited)
                self.search_board(results, board, visited,i2,j2, node.connections.get(board[i2][j2]))
                visited.remove((i2,j2))