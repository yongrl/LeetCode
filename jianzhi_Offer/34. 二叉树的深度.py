'''
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        '''
        层次遍历
        :param pRoot:
        :return:
        '''
        if pRoot is None:
            return 0
        pre_level =[]
        cur_level = [pRoot]
        next_level = []
        count = 0
        while cur_level:
            count =+ 1
            nodes = cur_level.pop(0)
            if nodes.left:
                next_level.append(nodes.left)
            if nodes.right:
                next_level.append(nodes.right)
            nodes_pool = next_pool
            next_pool = []
        return count



