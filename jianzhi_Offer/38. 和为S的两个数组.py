'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。

思路：
因为是递增数组，可以采用和为S的连续正数序列的双指针方法。

先输出小值，再输出大值。

乘积最小的，为小值最小的

'''
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        high = len(array)-1
        low = 0
        while high>low:
            cur_sum = array[low]+array[high]
            if cur_sum == tsum:
                return [array[low],array[high]]
            elif cur_sum > tsum:
                high -= 1
            else:
                low += 1

        return []


