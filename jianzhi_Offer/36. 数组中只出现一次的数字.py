'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

思路：
异或，当数组中只有一个数字出现一次时，全部异或所有数字，则最后的结果为出现一次的数。
当数组中有两个出现一次时，异或的结果为这两个数的异或结果，根据这个异或值，判断那个位置不同，
并且根据该位置的不同值，将数组分为两组，每组包含一个出现一次的数。
'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):

        res = 0  #0 与任何值异或结果为本身
        for i in array:
            res = res^i

        index = self.getFirstBit1(res) #判断第（index+1）位是否相等，移动index位
        num_1 = 0
        num_2 = 0

        for j in array:
            if ((j>>index)&1)==1:
                num_1 ^= j
            else:
                num_2 ^= j

        return [num_1,num_2]

    def getFirstBit1(self,res):

        index = 0    #index初始值为1

        while(res&1==0 and index < 32):
            res = res>>1
            index +=1

        return index


print(Solution().FindNumsAppearOnce([2,4,3,6,3,2,5,5]))

