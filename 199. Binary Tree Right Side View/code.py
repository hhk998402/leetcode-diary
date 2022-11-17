# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    rightMostView = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        depthOfTree = self.getDepthOfTree(root)
        self.rightMostView = [None for x in range(depthOfTree)]
        depth = 0
        self.findRightmostElementAtLevel(root, depth)
        return self.rightMostView

    
    def findRightmostElementAtLevel(self,root,depth):
        if(not root):
            return False
        if(self.rightMostView[depth] == None):
            self.rightMostView[depth] = root.val
        self.findRightmostElementAtLevel(root.right,depth+1)
        self.findRightmostElementAtLevel(root.left,depth+1)
        print(self.rightMostView)
                
        
    def getDepthOfTree(self, root):
        if(not root):
            return 0
        l_depth = self.getDepthOfTree(root.left)
        r_depth = self.getDepthOfTree(root.right)
        if(l_depth > r_depth):
            return l_depth+1
        else:
            return r_depth+1