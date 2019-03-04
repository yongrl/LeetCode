'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
因为python的int是无线精度的，c++的int是32为的，所以python的负数相当于前面有无限个1，要对python的负数做处理
'''

class Solution:
    def NumberOf1(self, n):
        # f=1
        # c = 0
        # for _ in range(32): #因为python是无限精度，所以不能while(flag),会一直有循环下去，只能截取32位
        #     if f&n>=1:
        #         c+=1
        #     f = f<<1
        # return c

        c = 0
        if n<0:
            n = n&0xffffffff
        while n:
            c += 1
            n &= n-1
        return c

