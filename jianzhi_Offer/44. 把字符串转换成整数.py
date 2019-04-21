'''
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。
数值为0或者字符串不是一个合法的数值则返回0。
'''

class Solution:
    def StrToInt(self, s):
        n = len(s)
        label = 1
        if n<=0:
            return 0

        if s[0]=='-':
            label = -1

        start = 1 if s[0]=='-' or s[0]=='+' else 0

        sum = 0

        for i in range(start,n):
            if s[i]>'0' and s[i]<'9':
                # (sum<<1)+(sum<<3)=sum*10, 但是这边注意+的优先级高于<<
                # python中字符串相减，不能用做ascii码相减，需要人工转换
                sum = (sum<<1) + (sum <<3) + ord(s[i])-ord('0')
            else:
                return 0

        return label*sum


print(Solution().StrToInt('-123'))



