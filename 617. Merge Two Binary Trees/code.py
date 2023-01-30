# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        newRoot = TreeNode()
        if not root1 and not root2:
            return None
        self.dfs(root1,root2,newRoot)
        return newRoot
    
    def dfs(self,root1,root2,newRoot):
        newRoot.left = TreeNode()
        newRoot.right = TreeNode()
        if(root1 and root2):
            newRoot.val = root1.val + root2.val
            newRoot.left = self.dfs(root1.left, root2.left, newRoot.left)
            newRoot.right = self.dfs(root1.right, root2.right, newRoot.right)
        elif root1 and not root2:
            newRoot.val = root1.val
            newRoot.left = self.dfs(root1.left, None, newRoot.left)
            newRoot.right = self.dfs(root1.right, None, newRoot.right)
        elif not root1 and root2:
            newRoot.val = root2.val
            newRoot.left = self.dfs(None, root2.left, newRoot.left)
            newRoot.right = self.dfs(None, root2.right, newRoot.right)
        else:
            return None
        return newRoot