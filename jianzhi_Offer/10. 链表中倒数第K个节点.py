'''
输入一个链表，输出该链表中倒数第k个结点。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # if head is None or k <= 0:
        #     return None
        # index = 0
        # node_index = head
        # while(node_index.next is not None):
        #     if index < k-1:
        #         index +=1
        #         node_index = node_index.next
        #
        # if index< k-1:
        #     return None
        # k_index = head
        #
        # while(node_index.next is not None):
        #     k_index = k_index.next
        #     node_index = node_index.next
        # return k_index

        if head is None or k <= 0:
            return None
        index = 0
        node_index = head
        k_index = head

        while(node_index.next is not None):
            node_index = node_index.next
            index +=1
            if index >= k-1:
                k_index = k_index.next
        if index >=k :
            return None
        else:
            return k_index