'''
输入一个链表，反转链表后，输出新链表的表头。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead

        pre = None
        curr = pHead

        while curr is not None:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        return pre