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

        cur_level = [pRoot]
        count = 0

        while cur_level:
            count += 1
            temp = cur_level
            cur_level = []

            for node in temp:
                if node.left:
                    cur_level.append(node.left)
                if node.right:
                    cur_level.append(node.right)
        return count

    def TreeDepth_1(self,pRoot):
        '''
        深度优先遍历
        :param pRoot:
        :return:
        '''

        if pRoot is None:
            return 0

        return max(self.TreeDepth_1(pRoot.left),self.TreeDepth_1(pRoot.right))+1




