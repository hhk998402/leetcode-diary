# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.counter = 0
        self.L = []
        self.val = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root,k)
        print(self.L, self.val)
        return self.val
    
    def dfs(self, node, k):
        if not node:
            return -1
        val = self.dfs(node.left,k)
        if val == -1:
            self.counter += 1
            self.L.append(node.val)
            if k == self.counter:
                self.val = node.val
                return node.val
        val = self.dfs(node.right,k)
        return val