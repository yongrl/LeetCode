'''
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1

        # 递归方法
        # if pHead1.val<=pHead2.val:
        #     listNode = pHead1
        #     listNode.next = self.Merge(pHead1.next, pHead2)
        #
        # else:
        #     listNode = pHead2
        #     listNode.next = self.Merge(pHead1,pHead2.next)
        # return listNode

        #非递归方法
        listNode = ListNode(0)
        p = listNode
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val <= pHead2.val:
                listNode.next = pHead1
                pHead1 = pHead1.next
            else:
                listNode.next = pHead2
                pHead2 = pHead2.next
            listNode = listNode.next

        if pHead1 is not None:
            listNode.next = pHead1
        if pHead2 is not None:
            listNode.next = pHead2

        return p.next

pHead1 = ListNode(1)
node3 = ListNode(3)
node5 = ListNode(5)

pHead2 = ListNode(2)
node4 = ListNode(4)
node6 = ListNode(6)

pHead1.next = node3
node3.next=node5
node5.next=None

pHead2.next=node4
node4.next=node6
node6.next=None

print(Solution.Merge(pHead1,pHead2))



