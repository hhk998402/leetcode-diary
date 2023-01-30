# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root,None)
        return len(self.res)
    
    def dfs(self, node, max1):
        if max1 == None:
            max1 = node.val
        if not node:
            return
        # print(node.val, self.res, max1)
        
        if(node.val >= max1):
            max1 = node.val
            self.res.append(max1)

        self.dfs(node.left, max1)
        self.dfs(node.right, max1)