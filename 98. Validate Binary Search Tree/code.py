# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(-inf, +inf, root)
    
    def dfs(self,leftLim, rightLim, node):
        if(not node):
            return True
        if(node.val <= leftLim or node.val >= rightLim):
            return False
        return self.dfs(leftLim, node.val, node.left) and self.dfs(node.val, rightLim, node.right)