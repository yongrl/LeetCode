# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if (s is None) &(t is None):
            return True
        if (s is None) | (t is None):
            return False
        return self.isSubtreeFromNode(s,t) | self.isSubtree(s.left,t) | self.isSubtree(s.right,t)

    def isSubtreeFromNode(self,s,t):
        if (s is None) &(t is None):
            return True
        if (s is None) | (t is None):
            return False
        if s.val != t.val:
            return False
        return self.isSubtreeFromNode(s.left,t.left)&self.isSubtreeFromNode(s.right,t.right)