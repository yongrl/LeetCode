'''
输入一颗二叉树，判断是否为平衡二叉树

平衡二叉树（Balanced Binary Tree），具有以下性质：
它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。

方法一：
运用递归法求二叉树深度的方法

方法二：
方法一又一个很明显的缺点，在判断上层节点的时候，会多次遍历下层节点，增加了不必要的开销。
如果改为从下网上遍历，如果子树是平衡二叉树，则返回子树的高度，如果发现子树不是平衡二叉树，
则直接停止遍历，这样至多只对每个节点访问一次
'''

class Solution:
    def IsBalanced_Solution(self, pRoot):

        # if pRoot is None:
        #     return True
        #
        # left = self.tree_depth(pRoot.left)
        # right = self.tree_depth(pRoot.right)
        #
        # return abs(left-right)<=1 & self.IsBalanced_Solution(pRoot.left) & \
        #        self.IsBalanced_Solution(pRoot.right)
        return self.getDepth(pRoot)!=-1

    def tree_depth(self, pRoot):
        if pRoot is None:
            return 0
        return max(self.tree_depth(pRoot.left),self.tree_depth(pRoot.right))+1


    def getDepth(self,pRoot):
        '''
        方法二
        :param pRoot:
        :return:
        '''

        if pRoot is None:
            return 0
        left = self.getDepth(pRoot.left)
        right = self.getDepth(pRoot.right)

        if left==-1:
            return -1
        if right == -1:
            return -1

        return  -1 if abs(left-right)>1 else 1+max(left,right)





