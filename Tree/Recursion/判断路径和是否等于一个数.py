# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#字底向上
# Runtime: 84 ms, faster than 1.61% of Python online submissions for Path Sum.

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        pathsum = self.pathSum(root)
        if sum in pathsum:
            return True
        else:
            return False

    def pathSum(self,root):
        if root is None:
            return []
        elif (root.left is None)&(root.right is not None):
            rightsum = self.pathSum(root.right)
            return [root.val + x for x in rightsum]
        elif (root.left is not None)&(root.right is None):
            leftsum = self.pathSum(root.left)
            return [root.val + x for x in leftsum]
        elif (root.left is None) & (root.right is None):
            return [root.val]
        else:
            leftsum = self.pathSum(root.left)
            rightsum = self.pathSum(root.right)
            return [root.val+x for x in leftsum+rightsum]


#Runtime: 60 ms, faster than 11.44% of Python online submissions for Path Sum.
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if (root.left is None)&(root.right is None)&(root.val==sum):
            return True
        else:
            return self.hasPathSum(root.left,sum-root.val) | self.hasPathSum(root.right,sum-root.val)
