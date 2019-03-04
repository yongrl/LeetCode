'''
输入一个链表，反转链表后，输出新链表的表头。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        pre = None
        while pHead:
            temp = pHead.next
            pHead.next = temp
            pre = pHead
            pHead = temp

        return pre


    last = None

    while pHead:
        tmp = pHead.next
        pHead.next = last
        last = pHead
        pHead = tmp
    return last

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
head = Solution().ReverseList(n1)
print(head.val)
print(head.next.val)