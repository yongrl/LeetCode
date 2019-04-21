'''
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

思路：双指针
一个指针指向开始数值，另一个数值指向结束，如果当前和小于sum,大指针向后移，否则，小指针向后移

注意边界条件，数字本身不算一个结果

'''
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum==1:
            return []
        low = 1
        high = 2
        sum = 3
        res = []

        while high > low:
            if sum == tsum:
                res.append([i for i in range(low,high+1)])
                high += 1
                sum += high
            elif sum < tsum:
                high += 1
                sum += high
            else:
                sum -= low
                low += 1
        return res

print(Solution().FindContinuousSequence(3))
