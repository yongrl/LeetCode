'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        res = []
        que= [root]
        while que:
            node = que.pop(0)
            res.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return res

#{10,6,14,4,8,12,16}
n1 =  TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left=n2
n1.right=n3
print(Solution().PrintFromTopToBottom(n1))