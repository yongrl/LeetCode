# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self,path=0):
        self.path = path

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.path

    def dfs(self,root):
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if root.left is not None:
            if root.left.val == root.val:
                leftPath = left+1
            else:
                leftPath = 0

        if root.right is not None:
            if root.right.val == root.val:
                rightPath = right+1
            else:
                rightPath = 0

        self.path = max(self.path,leftPath+rightPath)
        return max(leftPath,rightPath)
