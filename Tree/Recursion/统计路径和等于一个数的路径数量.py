# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return self.pathSumWithRoot(root,sum)+\
                   self.pathSum(root.left,sum)+\
                   self.pathSum(root.right,sum)

    def pathSumWithRoot(self,root,sum):
        res = 0
        if root is None:
            return res
        if root.val==sum:
            res+=1
        res+= self.pathSumWithRoot(root.left,sum-root.val)+\
              self.pathSumWithRoot(root.right,sum-root.val)
        return res