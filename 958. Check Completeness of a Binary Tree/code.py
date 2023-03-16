import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.levelOrder = collections.defaultdict(lambda:0)

    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height = self.findHeight(root, 0)
        for i in range(1,height+1):
            #Each level has 2^(i-1) nodes.
            #Special case of last row is handled separately
            self.levelOrder[i] = 2**(i-1)
        print(height)
        queue = [(root, 1)]
        lastRow = []
        while(queue):
            node, level = queue.pop(0)
            left = node.left
            right = node.right
            self.levelOrder[level] -= 1
            #In order to check if the lastRow is in left-most order
            if level == height - 1:
                lastRow.append(left)
                lastRow.append(right)
            if left:
                queue.append((left,level+1))
            if right:
                queue.append((right,level+1))
        
        for i in range(1,height):
            if self.levelOrder[i] != 0:
                return False
        
        # Special case of last row where once a null value is encountered, 
        # we will go the rest of the row to ensure it is all null values from
        # that point on
        nullVal = None
        for val in lastRow:
            if not val:
                if nullVal == None:
                    nullVal = True
            else:
                if nullVal:
                    return False
        return True
    
    #Find height of binary tree
    def findHeight(self,node,level):
        if node:
            level += 1
        else:
            return level
        return max([level,self.findHeight(node.left, level),self.findHeight(node.right, level)])
