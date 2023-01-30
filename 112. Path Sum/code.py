# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(not root):
            return False
        self.dfs(root,0,targetSum)
        return self.flag
    
    def dfs(self,node,s,target):
        print(s)
        if(self.flag):
            return
        if node and not node.right and not node.left:
            if(s + node.val == target):
                self.flag = True
        elif node:
            self.dfs(node.left, s + node.val, target)
            self.dfs(node.right, s + node.val, target)
        return
        
