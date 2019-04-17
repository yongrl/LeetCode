'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,
可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
'''
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        numbers = []
        while n>0:
            numbers.append(n%10)
            n=n//10
        return numbers

        num_size = len(numbers)
        count = 0
        for index,num in enumerate(numbers):
            if num==0:
                num=9
            for i in range(index,1,-1):
                return


print(Solution().NumberOf1Between1AndN_Solution(1300))