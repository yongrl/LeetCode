'''
判断链表是否存在环

141. Linked List Cycle (Easy)

使用双指针，一个指针每次移动一个节点，一个指针每次移动两个节点，如果存在环，那么这两个指针一定会相遇。
'''
class ListNode(object):
    def __init__(self,value,next):
        self.value=value
        self.next=next

def hasCycle(listnode):
    if listnode==None:
        return False
    p1=listnode
    p2=listnode.next
    while(p1!=None & p2!=None & p2.next!=None):
        if p1==p1:
            return True
        else:
            p1=p1.next
            p2=p2.next.next
    return False
