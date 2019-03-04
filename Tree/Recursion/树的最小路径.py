# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 超时
# class Solution(object):
#     def minDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root is None:
#             return 0
#         left = self.minDepth(root.left)
#         right = self.minDepth(root.right)
#         if(left==0)|(right==0):
#             return left+right+1
#
#         return min(self.minDepth(root.left),self.minDepth(root.right))+1

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if(left==0)|(right==0):
            return left+right+1

        return min(self.minDepth(root.left),self.minDepth(root.right))+1

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        level=1
        queue_level=[root]

        while queue_level:
            tmp=[]
            for curr in queue_level:
                if (curr.left is None) & (curr.right is None):
                    return level
                if curr.left:
                    tmp.append(curr.left)
                if curr.right:
                    tmp.append(curr.right)
            level+=1
            queue_level=tmp
        return level




