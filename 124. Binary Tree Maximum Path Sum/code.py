# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxSum = None

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root,0)
        return self.maxSum if self.maxSum else 0    
        
    def dfs(self, root, sum):
        if(not root):
            return 0
        leftSum = self.dfs(root.left, sum)
        rightSum = self.dfs(root.right, sum)
        val = root.val
        print(leftSum, rightSum, val)
        possibleSums = set([val, val+leftSum, val+rightSum, val+rightSum+leftSum])
        if(0 in possibleSums):
            possibleSums.remove(0)
        print(possibleSums)
        if(len(possibleSums) <= 0):
            return sum
        sum = max(possibleSums)
        if(not self.maxSum or sum > self.maxSum):
            self.maxSum = sum
        return max(val, val+leftSum, val+rightSum)
