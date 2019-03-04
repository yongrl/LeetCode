# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self, max=0):
        self.max = max

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxDepth(root)
        return self.max

    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            lm = self.maxDepth(root.left)  # 求左边的最大路径
            rm = self.maxDepth(root.right)
            self.max = max(self.max, lm + rm)  # 求该节点的最大半径
            return max(lm, rm) + 1  # 求最大路径

