# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#又超时
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        val1 = root.val

        if root.left is not None:
            val1 += self.rob(root.left.left)+self.rob(root.left.right)
        if root.right is not None:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)

        val2 = self.rob(root.left)+self.rob(root.right)

        return max(val1,val2)

#层次遍历
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        q=[root]
        level = 1
        val1=0
        val2=0
        while True:
            temp = []
            while q:
                node = q.pop(0)
                if(level%2==0):
                    val1+=node.val
                if(level%2==1):
                    val2+=node.val
                if node.left is not None:
                    temp.append(node.left)
                if node.right is not None:
                    temp.append(node.right)
            if len(temp)==0:
                break
            else:
                q=temp
        return max(val1,val2)




