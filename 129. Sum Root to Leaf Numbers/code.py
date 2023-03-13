# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, "")
    
    def dfs(self,node,num):
        if not node:
            return None
        
        num += str(node.val)
        leftSum = self.dfs(node.left, num)
        rightSum = self.dfs(node.right, num)
        if not leftSum and not rightSum:
            return int(num)
        elif not leftSum:
            return rightSum
        elif not rightSum:
            return leftSum
        else:
            return leftSum + rightSum