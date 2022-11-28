class Node:
    def __init__(self):
        self.added = False
        self.connections = {}

class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        self.insertRecursive(self.root, word, 0)
    
    def insertRecursive(self, root, word, idx):
        letter = word[idx]
        if(letter not in root.connections):
            root.connections[letter] = Node()
        # print("Recursive", letter, root.connections, root.added)
        if(idx == len(word)-1):
            root.connections[letter].added = True
        else:
            self.insertRecursive(root.connections[letter], word, idx+1)

    def search(self, word: str) -> bool:
        curNode = self.root
        idx = 0
        for idx in range(0,len(word)):
            letter = word[idx]
            # print(word, letter, curNode.connections, curNode.added)
            if(letter not in curNode.connections):
                return False
            curNode = curNode.connections[letter]
        # print("Outside search", word, idx, curNode.connections, curNode.added)
        return curNode.added

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for idx in range(0,len(prefix)):
            letter = prefix[idx]
            if(letter not in curNode.connections):
                return False
            curNode = curNode.connections[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)