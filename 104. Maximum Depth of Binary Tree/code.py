# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root,1,0)
    
    def dfs(self, node, currLevel, maxLevel):
        if(not node):
            return maxLevel
        if(currLevel > maxLevel):
            maxLevel = currLevel
        currLevel += 1
        maxLevel = self.dfs(node.left, currLevel, maxLevel)
        maxLevel = self.dfs(node.right, currLevel, maxLevel)
        return maxLevel