'''
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root is None :
            return []
        self.res = []
        self.expectNumber = expectNumber
        self.FindPathSum(root,0,[])
        return self.res

    def FindPathSum(self,root,currSum,path):
        currSum += root.val
        path.append(root)

        isLeaf = root.left is None and root.right is None
        if currSum ==  self.expectNumber and isLeaf:
            one_path = []
            for node in path:
                one_path.append(node.val)
            self.res.append(one_path)
        elif currSum<self.expectNumber:
            if root.left:
                self.FindPathSum(root.left,currSum,path)
            if root.right:
                self.FindPathSum(root.right,currSum,path)
        path.pop()





