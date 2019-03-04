'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

*1.当底数为0且指数<0时
*会出现对0求倒数的情况，需进行错误处理，设置一个全局变量；
*2.判断底数是否等于0
*由于base为double型，不能直接用==判断
*3.优化求幂函数
*当n为偶数，a^n =（a^n/2）*（a^n/2）
*当n为奇数，a^n = a^[(n-1)/2] * a^[(n-1)/2] * a
*时间复杂度O(logn)
'''
class Solution:
    def Power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        # if exponent<0:
        #     res = 1
        #     for i in range(-exponent):
        #         res *= base
        #     return 1/res
        # if exponent>0:
        #     res = 1
        #     for i in range(exponent):
        #         res *= base
        #     return res           #30ms

        #优化幂运算
        e = abs(exponent)
        res = 1
        temp = base
        while(e>0):
            if e&1 ==1:
                res *= temp

            e = e>>1
            temp = temp*temp
        return res if exponent>0 else 1/res    #41ms


s = Solution().Power(2,3)
print(s)

