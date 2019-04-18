'''
输入两个链表，找出它们的第一个公共结点。
@Author: yongrl
@Date: 2019/04/18
'''

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 is None or pHead2 is None:
            return None
        len1 = self.getListLength(pHead1)
        len2 = self.getListLength(pHead2)

        longP = pHead1
        shortP = pHead2
        diff = len1 - len2


        if len2 > len1:
            longP = pHead2
            shortP = pHead1
            diff = len2 - len1

        for i in range(diff):
            longP = longP.next

        # longP = shortP会退出循环，如果运行到最后的，则认为没有公共点，返回None
        while(longP is not None and shortP is not None and longP!=shortP):
            longP = longP.next
            shortP = shortP.next

        return longP

    def getListLength(self,pHead):

        p = pHead
        length = 0

        while(p):

            length += 1
            p = p.next

        return length

