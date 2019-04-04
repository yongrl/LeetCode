'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence is None or len(sequence)==0:
            return False
        if len(sequence)==1:
            return True
        root = sequence[-1]
        mid = 0
        for i in sequence:
            if i < root:
                mid+=1
            else:
                break
        for i in sequence[mid:-1]:
            if i < root:
                return False
        left = True
        if mid>0:  ##注意mid=0时,左边的序列为[],题目要求[]应当返回false，所以这边要在进入子程序时，先对mid进行判断
            left = self.VerifySquenceOfBST(sequence[0:mid])
        right = True
        if mid<len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[mid:-1])
        return  left and right


print(Solution().VerifySquenceOfBST([]))