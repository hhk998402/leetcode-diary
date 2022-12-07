# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root,low,high)

    def dfs(self, root, low, high):
        if not root:
            return 0

        if(not (root.val >= low and root.val <= high)):
            return self.dfs(root.left,low,high) + self.dfs(root.right,low,high)
            
        return root.val + self.dfs(root.left,low,high) + self.dfs(root.right,low,high)
