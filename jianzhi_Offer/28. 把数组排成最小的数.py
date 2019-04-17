'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

@athor: yongrl
@data: 2019/4/17

Solution
the result is the concat of a order of the list,so order the numbers in the list.

the rule of the sort is as follows:
if ab>ba,then a>b
if ab=ba,then a=b
if ab<ba,then a<b

the result is the concat of
'''

class Solution:
    def PrintMinNumber(self, numbers):
        # if not sure about the return value of the special case, should ask
        # it is better to consider all the posible cases
        if numbers is None or len(numbers)==0:
            return ''

        numbers = [str(i) for i in numbers]
        for i in range(len(numbers)):
            for j in range(len(numbers)-1,i,-1):
                if self.strComparetor(numbers[i],numbers[j]):
                    temp = numbers[j]
                    numbers[j] = numbers[i]
                    numbers[i] = temp
        res = int(''.join(numbers))
        return res

    def strComparetor(self,str_a,str_b):
        if str_a+str_b >= str_b+str_a:
            return True
        else:
            return False


print(Solution().PrintMinNumber([3,32,321]))