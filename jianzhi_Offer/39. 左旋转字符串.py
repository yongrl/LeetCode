'''
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。

思路：
这边简单的字符串截取和拼接就可以实现，但是面试官想要考察的是字符串的反转。
假设S=XY，（XTYT）T即为左移后的字符串，这边和矩阵的转置操作的运算规律是一致的。

这边需要注意的是，如题中的S，循环左移3位和循环左移12位（12位体现了题目中的循环）结果是一致的。
所有判断旋转位数时要取余

'''
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):

        if len(s) == 0: return s

        n = n % len(s)

        x = ''.join([s[x] for x in range(n-1,-1,-1)])

        y = ''.join([s[y] for y in range(len(s)-1,n-1,-1)])

        st = x+y

        return ''.join([st[i] for i in range(len(s)-1,-1,-1)])


print(Solution().LeftRotateString('abcXYZdef', 3))
