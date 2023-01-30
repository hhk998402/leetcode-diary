# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.preOrder(root, "")

    def preOrder(self, node, s):
        if not node:
            return s
        s = str(node.val)
        if node.left:
            s += "(" + self.preOrder(node.left, s) + ")"
        if node.right:
            if not node.left:
                s += "()"
            s += "(" + self.preOrder(node.right, s) + ")"
        return s