# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)
        
    
    def dfs(self, left, right):
        #If both left and right are None
        if not left and not right:
            return True
        #If either one is None
        elif (not left and right) or (not right and left):
            return False
        #If the value is not the same
        elif left.val != right.val:
            return False
        #Recurse
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
