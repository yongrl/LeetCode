# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = True    #注意类内的全局变量的定义

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.maxDepth(root)
        return self.result

    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            ml = self.maxDepth(root.left)
            mr = self.maxDepth(root.right)
            if abs(ml - mr) > 1:
                self.result = False
            return max(ml, mr) + 1

