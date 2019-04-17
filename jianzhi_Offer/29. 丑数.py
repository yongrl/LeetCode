'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

思路:
丑数可以表述成2^a*3^b*5^c的形式，一个丑数由a+b+c个因子组成，
每增加一个因子时有三个选择，分别为2，3, 5，但是当前只能选择最小的一个存入最后的
结果集中，未被选中的则进入候选集，此时因此个数a+b+c仍然为n,
而进入结果集的丑数a+b+c序列会产生三个新的候选集序列（a+1,b,c）,(a,b+1,c),(a,b,c+1)

如果将这些候选集全部放在一个list中，后需要一个排序操作，
这边有一个技巧：使用三个list来分别存储*2,*3,*5得到的丑数候选列，
因为由一个乘子生成的候选列必然是有序的，避免了排序操作

'''

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index<=0:
            return 0
        res=[1]
        cur_min=1
        que_2,que_3,que_5=[],[],[]
        while len(res)<index:
            a,b,c = cur_min*2,cur_min*3,cur_min*5
            que_2.append(a)
            que_3.append(b)
            que_5.append(c)
            min_2,min_3,min_5 = que_2[0],que_3[0],que_5[0]
            cur_min=self.min_3(min_2,min_3,min_5)
            res.append(cur_min)
            if min_2==cur_min:
                que_2.pop(0)
            if min_3==cur_min:
                que_3.pop(0)
            if min_5==cur_min:
                que_5.pop(0)
        return res[-1]

    def min_3(self,min_2,min_3,min_5):
        return min(min(min_2,min_3),min_5)


print(Solution().GetUglyNumber_Solution(5))