# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    LCA = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pVal = min([p.val,q.val])
        qVal = max([p.val,q.val])
        self.traceCommonAncestor(root, pVal, qVal)
        return self.LCA
        
    def traceCommonAncestor(self, root, p, q):
        if(not root):
            return False
        if(self.LCA == None):
            self.LCA = root

        if(root.val >= p and root.val <= q):
            self.LCA = root
            return True
        elif(root.val > p and root.val > q):
            self.LCA = root
            self.traceCommonAncestor(root.left, p, q)
        elif(root.val < p and root.val < q):
            self.LCA = root
            self.traceCommonAncestor(root.right, p, q)
        elif(root.val == p or root.val == q):
            self.LCA = root
            return True
        else:
            return False
