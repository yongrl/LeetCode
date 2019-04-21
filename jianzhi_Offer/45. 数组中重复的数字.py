'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
  那么对应的输出是第一个重复的数字2。

思路：
1。 剑指offer的思路：
 * 思路：
 * 数组中的数字都在0到n-1的数字范围内。如果数组中没有重复出现的数字，那么当数组排序后数字i就出现在数组中下标为i的元素处。那么数组中如果存在重复数字的话，有些位置的对应的数字就没有出现，而有些位置可能存在多个数字。数组用numbers表示
 那么我们重排这个数组。从第0个元素开始。
 1、比较numbers[i]和i的值，如果i与numbers[i]相等，也就是对数组排序后，numbers[i]就应该在对应的数组的第i个位置处，那么继续判断下一个位置。
 2、如果i和numbers[i]的值不相等，那么判断以numbers[i]为下标的数组元素是什么。
 2.1、如果numbers[numbers[i]]等于numbers[i]的话，那么就是说有两个相同的值了，重复了。找到了重复的数字
 2.2、如果numbers[numbers[i]]不等于numbers[i]的话，那么就将numbers[numbers[i]]和numbers[i]互换。继续进行1的判断。
 3、循环退出的条件是直至数组最后一个元素，仍没有找到重复的数字，数组中不存在重复的数字。

2。hash方法：


'''
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if numbers is None or len(numbers)==0:
            return False

        for i in range(len(numbers)):
            if numbers[i] == i:
                continue
            else:
                if numbers[numbers[i]] == numbers[i]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    temp = numbers[numbers[i]]
                    numbers[numbers[i]] = numbers[i]
                    numbers[i] = temp

        return False


print(Solution().duplicate([2, 1, 3, 1, 4], [-1]))
