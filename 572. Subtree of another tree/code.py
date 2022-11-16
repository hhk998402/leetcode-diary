# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        print(root.val if root else "EmptyRoot", subRoot.val if subRoot else "Empty SubRoot")
        #Case 1: root and subRoot are null
        if(not root and not subRoot):
            return True
        #Case 2: root and subRoot are both non-null
        if(not root or not subRoot):
            return False
        #Case 3: Recursive check for left sub-tree and right-subtree 
        if(self.areTreesSame(root, subRoot)):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def areTreesSame(self, root1, root2):
        if(not root1 and not root2):
            return True
        if(not root1 or not root2):
            return False
        if(root1.val != root2.val):
            return False
        return self.areTreesSame(root1.left, root2.left) and self.areTreesSame(root1.right, root2.right)
        