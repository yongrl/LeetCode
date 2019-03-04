'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
# -*- coding:utf-8 -*-



#入队时，判断stack1是否为空，如不为空，将元素压入stack1；如为空，先将stack2元素倒回stack1，再将新元素压入stack1

#出队时，判断stack2是否为空，如不为空，则直接弹出顶元素；如为空，则将stack1的元素逐个“倒入”stack2，
# 把stack1最后一个元素弹出并出队。
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, node):
        if len(self.stack1)==0:
            while len(self.stack2)>0:
                self.stack1.append(self.stack2.pop())
        self.stack1.append(node)

    def pop(self):
        if len(self.stack2)==0:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

# return xx
s = Solution()
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.pop())
print(s.pop())
print(s.push(4))
print(s.pop())
print(s.push(5))
print(s.pop())
print(s.pop())
