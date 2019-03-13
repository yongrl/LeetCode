'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
思路：构建一个辅助栈用来存储当前的最小值
'''
class Solution:
    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, node):
        min = self.min()
        if not min or node < min:

            self.minStack.append(node)
        else:
            self.minStack.append(min)

        self.mainStack.append(node)


    def pop(self):
        if self.mainStack:
            self.minStack.pop()
            return self.mainStack.pop()

    def top(self):
        if self.mainStack:
            return self.mainStack[-1]

    def min(self):
        if self.minStack:
            return self.minStack[-1]

