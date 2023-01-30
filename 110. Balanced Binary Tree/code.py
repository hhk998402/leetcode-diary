# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, depth):
            if not node:
                return 0
            if depth < 0:
                return -1
 
            leftDepth = dfs(node.left, depth)
            rightDepth = dfs(node.right, depth)
            if abs(leftDepth - rightDepth) > 1 or leftDepth < 0 or rightDepth < 0:
                return -1
            return 1+max(leftDepth, rightDepth)
            

        return dfs(root, 0) >=0